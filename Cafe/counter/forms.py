from django import forms
from .models import Cashier
class CashierForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Cashier
        fields = ['username', 'password' ]
