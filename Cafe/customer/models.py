from django.db import models
from django.forms import ModelForm

# Create your models here.


class Customer_Details(models.Model):
    table_no = models.IntegerField(unique=True, error_messages={'unique':"TABLE IS OCCUPIED: Kindly choose another table :)"})
    customer_name = models.CharField(max_length=50)
    mobile_no= models.CharField(max_length=15)

    class Meta:
        verbose_name = ("Customer_Details")
        verbose_name_plural = ("Customer_Details")

    def __str__(self):
        return self.customer_name


class Table_Orders(models.Model):
    table_no = models.IntegerField(default=None, blank=True)
    food = models.CharField(max_length=50)
    price = models.IntegerField(default=None)
    quantity = models.IntegerField(default=None, blank=True)
    total = models.IntegerField(default=None, blank=True)

    class Meta:
        verbose_name = ("Table_Order")
        verbose_name_plural = ("Table_Orders")

    def __str__(self):
        return self.table_no

class Reviews(models.Model):
    table_no = models.IntegerField(default=None, blank=True)
    phone_no = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    rate = models.CharField(max_length=15)
    comment = models.TextField(max_length=100)

    class Meta:
        verbose_name = ("Reviews")
        verbose_name_plural = ("Reviews")

    def __str__(self):
        return self.Name
