# forms.py
from django import forms

class CheckoutForm(forms.Form):
    email_or_phone = forms.CharField(max_length=100)
