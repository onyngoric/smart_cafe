from django import forms
from django.forms import ModelForm
from .models import Customer_Details, Table_Orders, Reviews
     
class Customer_Details_Form(forms.ModelForm):
    class Meta:
        model = Customer_Details
        fields = ['table_no', 'customer_name', 'mobile_no',]
    
class Table_Orders_Form(forms.ModelForm):
    class Meta:
        model = Table_Orders
        fields = ['food', 'price', 'quantity',]

class Reviews_Form(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['table_no', 'phone_no', 'name', 'rate', 'comment']
