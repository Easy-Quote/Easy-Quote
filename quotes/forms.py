from django import forms

from .models import Quote202

class Quote101(forms.ModelForm):
    quote_number = forms.IntegerField()
    quote_customer = forms.CharField(max_length=200)
    quote_address = forms.CharField(max_length=200)
    quote_employee = forms.CharField(max_length=200)
    quote_totoal_price = forms.CharField(max_length=200)
    quote_items_code = forms.CharField(max_length=2000)
    class Meta:
        model = Quote202
        fields = [
            'quote_number',
            'quote_customer',
            'quote_address',
            'quote_employee',
            'quote_totoal_price',
            'quote_items_code',
        ]

# class quote_form(forms.Form):
#     quote_number = forms.IntegerField()
#     quote_customer = forms.CharField(max_length=200)
#     quote_address = forms.CharField(max_length=200)
#     quote_employee = forms.CharField(max_length=200)
#     quote_totoal_price = forms.CharField(max_length=200)
#     quote_items_code = forms.CharField(max_length=2000)