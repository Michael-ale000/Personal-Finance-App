from django import forms

class searchform(forms.Form):
    min_price = forms.DecimalField(label='Minimum Price', required=False)
    max_price = forms.DecimalField(label='Maximum Price', required=False)
    min_pe_ratio = forms.DecimalField(label='Minimum P/E Ratio', required=False)
    max_pe_ratio = forms.DecimalField(label='Maximum P/E Ratio', required=False)