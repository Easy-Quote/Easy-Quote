from django import forms
from .models import inventory

class Inventory1(forms.ModelForm):
    def Item1(self):
        item_code = forms.CharField(max_length=200)
        item_description = forms.CharField(max_length=200)
        item_price = forms.FloatField(max_length=200)

    class Meta:
        model = inventory
        fields = [
            'item_code',
            'item_description',
            'item_price',
        ]