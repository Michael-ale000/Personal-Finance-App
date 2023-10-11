from django import forms
from .models import stockportfolio
class addstockform(forms.ModelForm):
    stocksymbol=forms.CharField(max_length=10)
    stockname=forms.CharField(max_length=100)
    quantity=forms.IntegerField()
    buy_price=forms.IntegerField()
    class Meta:
        model=stockportfolio
        fields=('stocksymbol','stockname','quantity','buy_price')