from django.contrib import admin
from django.urls import include, path
from . import views
from .views import Pdf

urlpatterns = [
    path('login/', views.counter_login, name="counter_login"),
    path('passgen/', views.password_gen, name="password_gen"),
    path('orders/', views.counter_orders, name="counter_orders"),
    path('feedback/', views.feedback, name="feedback"),
    path('pdf/', Pdf.as_view(), name="pdf_view"),
    path('logout/', views.logout_view, name="logout_view"),
]
