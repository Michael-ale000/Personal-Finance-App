from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import User_Info,IncomeRecord

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['username'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'username', 
            'id':'username', 
            'type':'text', 
            'placeholder':'John Doe', 
            'maxlength': '16', 
            'minlength': '6', 
            }) 
        self.fields['email'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'email', 
            'id':'email', 
            'type':'email', 
            'placeholder':'JohnDoe@mail.com', 
            }) 
        self.fields['password1'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'password1', 
            'id':'password1', 
            'type':'password', 
            'placeholder':'password', 
            'maxlength':'22',  
            'minlength':'8' 
            }) 
        self.fields['password2'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'password2', 
            'id':'password2', 
            'type':'password', 
            'placeholder':'password', 
            'maxlength':'22',  
            'minlength':'8' 
            }) 
 
 
    username = forms.CharField(max_length=20, label=False) 
    email = forms.EmailField(max_length=100) 
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


# # Creating a form class for the expense
# class ExpenseForm(forms.Form):
  
#    # Defining the fields for the form
#    title = forms.CharField()
   
#    category = forms.CharField()
#    amount = forms.IntegerField()
  
#    # Defining the widgets for the form
#    widget = {
#        'title': forms.TextInput(attrs={'class': 'input-group form-control form-control-lg'}),
#        'amount': forms.TextInput(attrs={'class': 'input-group form-control form-control-lg'}), 
#    }
    

class TransactionForm(forms.ModelForm):
    # Define the choices for category and finance type
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('housing', 'Housing'),
        ('transportation', 'Transportation'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    ]

    FINANCE_TYPE_CHOICES = [
        ('income', 'Income'),
        ('expenditure', 'Expenditure'),
    ]

    title = forms.CharField(max_length=255)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    finance_type = forms.ChoiceField(choices=FINANCE_TYPE_CHOICES)

    class Meta:
        model = IncomeRecord # Replace 'Transaction' with your actual model name
        fields = ['title', 'amount', 'category', 'finance_type']
  
class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User