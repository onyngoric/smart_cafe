from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .render import Render
from django.utils import timezone
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from datetime import datetime
from .models import Password
from customer.models import Table_Orders, Reviews
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.

def counter_login(request):
	#render counter login page
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
		return HttpResponseRedirect(reverse('counter_orders'))
	return render(request, 'counter/counter_login.html')


def password_gen(request):
    	#render password generator page
		date_now_raw=datetime.now()
		date_now_str = datetime.strptime(str(date_now_raw), "%Y-%m-%d %H:%M:%S.%f")
		date_now = date_now_str.strftime("%Y-%m-%d")
		prev_date_raw = Password.objects.get(id="1")
		prev_date = prev_date_raw.today_date

		if date_now != prev_date:
    		#Generate Random Password
			random_password = get_random_string(length=10)
			Password.objects.all().filter(id='1').update(password=random_password) #update database with new password
			get_new_password = Password.objects.get(id='1')
			fial_new_password = get_new_password.password
			Password.objects.all().filter(id='1').update(today_date=date_now) #update Database with todays date
		else:
			get_new_password = Password.objects.get(id='1')
			fial_new_password = get_new_password.password

		return render(request, 'counter/password_gen.html', {"date": date_now, "password": fial_new_password})


def counter_orders(request):
    	#render counter orders page
	table_orders = Table_Orders.objects.all()
	if request.method == "POST":
		get_id = request.POST.get('id')
		Table_Orders.objects.all().filter(id=get_id).delete()
	return render(request, 'counter/counter_orders.html', {'table_orders':table_orders})


def feedback(request):
    	#render feedback page
	feedback = Reviews.objects.all()
	return render(request, 'counter/feedback.html', {'feedback': feedback})


def pdf_view(request):
    return HttpResponseRedirect(reverse('Pdf'))

class Pdf(View):
    
    def get(self, request):
        orders = Table_Orders.objects.all()
        today = timezone.now()
        params = {
            'today': today,
            'orders': orders,
            'request': request
        }
        return Render.render('counter/orderspdf.html', params)


def logout_view(request):
    logout(request)
    return redirect('counter_login')
