from django.contrib import admin
from django.urls import include, path
from . import views
from .views import customer_details, menu
from Cafe import settings

urlpatterns = [
    path('home/', views.customer_home, name="customer_home"),
    path('menu/', views.menu, name="menu"),
    # path('menu/', menu.as_view(), name="menu"),
    path('review/', views.customer_review, name="customer_review"),
    path('thanks/', views.thank_customer, name="thank_customer"),
    path('details/', customer_details.as_view(), name="customer_details"),
    # path('menu/', views.saveform, name="saveform")
]

