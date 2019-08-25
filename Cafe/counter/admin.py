from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Menu_items)
admin.site.register(Categories)
admin.site.register(Password)
admin.site.register(Customer_Order)
admin.site.register(Cashier)