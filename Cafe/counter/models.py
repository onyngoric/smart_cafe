from django.db import models
# from datetime import date

# Create your models here.

class Categories(models.Model):
    category_no = models.CharField(max_length=50, primary_key=True)
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.category_name

class Menu_items(models.Model):
    menu_no = models.CharField(max_length=50, primary_key=True)
    category_name = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name= models.CharField(max_length=50)
    picture = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None, default=None)
    description=models.TextField(max_length=50)
    price_per_item= models.IntegerField()
    select= models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Menu_item")
        verbose_name_plural = ("Menu_Items")

    def __str__(self):
        return self.name

class Password(models.Model):
    today_date = models.CharField(max_length=50, editable=False)
    password= models.CharField(max_length=50, editable=False, default="abcdefgh123456789")

    class Meta:
        verbose_name = ("Password")
        verbose_name_plural = ("Password")

class Customer_Order(models.Model):
    table_no = models.CharField(max_length=50, primary_key=True)
    name=models.CharField(max_length=50)
    quantity = models.IntegerField()
    phone_no = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Customer_Order")
        verbose_name_plural = ("Customer_Orders")

class Cashier(models.Model):
    username = models.CharField(max_length=50, primary_key=True, default=None)
    password = models.CharField(max_length=50, unique=True,default=None)

    class Meta:
        verbose_name = ("Cashier")
        verbose_name_plural = ("Cashier")

    def __str__(self):
        return self.username
