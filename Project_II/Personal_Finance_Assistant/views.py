from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate,login,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .form import SignUpForm,TransactionForm,CustomPasswordChangeForm
from .models import IncomeRecord
from django.db.models import Sum

# Create your views here.


def signin(request):
        try:
            form = SignUpForm()
            if request.method == "POST":
                form = SignUpForm(request.POST)   
                if form.is_valid():
                    form.save()
                    messages.success(request,"Account created sucessfully!")
                    return redirect("index")
                
            context = {'form':form}
            return render(request,'index.html',context)
        except IndexError:
            return redirect("index")


def log_in(request):
    try:
        if request.method =="POST":
            u_id = request.POST.get("username")
            pass_word = request.POST.get("password1")
            user = authenticate(request, username=u_id, password=pass_word)
        if user is not None:
            login(request, user)
            request.session['username'] = u_id #setting the session variable
            return redirect('landing')  # Change 'home' to the appropriate URL name
        messages.error(request,"Invalid Username or Password")
        return(redirect('index'))
    except:
        return redirect('index')

@login_required(login_url='index')
def landing(request):
    return render(request,'landingpage.html')



@login_required(login_url='index')    
def income_expenses(request):
    try:
            #print(request.session.get('username'))
            uname =  request.session.get('username')
            form = TransactionForm
            if request.method == "POST":
                form = TransactionForm(request.POST)   
                if form.is_valid():
                    incomerecord = IncomeRecord()
                    incomerecord.user = User.objects.get(username=uname)
                    incomerecord.category = form.cleaned_data['category']
                    incomerecord.title = form.cleaned_data['title']
                    incomerecord.amount = form.cleaned_data['amount']
                    incomerecord.finance = form.cleaned_data['finance_type']
                    incomerecord.save()
                    messages.success(request,"Data Stored sucessfully!")
                    #for transfering income expense form and icome expense data to template
                    # print(request.session.get('username'))
                    user_instance = User.objects.get(username=uname)
                    income_data = IncomeRecord.objects.filter(user=user_instance) #to get the user instance
                    # to calculate the income and expenditure
                    # Calculate the total income 
                    total_income = IncomeRecord.objects.filter(user=request.user, finance='Income').aggregate(total=Sum('amount'))['total']
                    total_expenditure = IncomeRecord.objects.filter(user=request.user, finance='Expenditure').aggregate(total=Sum('amount'))['total']
                    context = {'form':form,
                       'income_data':income_data,
                       'income':total_income,
                       'expenditure':total_expenditure}
                    redirect("income_expenses")
            #for transfering income expense form and icome expense data to template
           # print(request.session.get('username'))
            user_instance = User.objects.get(username=uname)
            income_data = IncomeRecord.objects.filter(user=user_instance) #to get the user instance
            # to calculate the income and expenditure
            # Calculate the total income 
            total_income = IncomeRecord.objects.filter(user=request.user, finance='Income').aggregate(total=Sum('amount'))['total']
            total_expenditure = IncomeRecord.objects.filter(user=request.user, finance='Expenditure').aggregate(total=Sum('amount'))['total']
            context = {'form':form,
                       'income_data':income_data,
                       'income':total_income,
                       'expenditure':total_expenditure}
            return render(request,'income_expenses.html',context)
    except Exception as e:
            return redirect("index")
@login_required(login_url='index')       
def delete_income(request, pk):
    income_record = get_object_or_404(IncomeRecord, pk=pk)

    # Check if the logged-in user is the owner of the income record
    if income_record.user == request.user:
        income_record.delete()

    # Redirect to the income list page
    return redirect('income_expenses')

#to change password
@login_required(login_url='index')
def settings(request):

            form = CustomPasswordChangeForm(request.user)
            if request.method == "POST":
                form = CustomPasswordChangeForm(request.user,request.POST)   
                if form.is_valid():
                    user=form.save()
                    update_session_auth_hash(request, user)
                    logout(request)
                    messages.success(request,"Password changed sucessfully!")
                    return redirect("index")
                
            context = {'form':form}
            return render(request,'settings.html',context)
    # except :
    #     return redirect("index")
    
#defining logout function 

def logout(request):
    try:
        request.session.clear()
        logout(request)
        return(redirect("index"))
    except BaseException as e:
            return redirect("index")