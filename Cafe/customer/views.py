import twilio
from twilio.rest import Client
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.forms import modelformset_factory
from .models import Customer_Details, Table_Orders, Reviews
from .forms import Customer_Details_Form, Table_Orders_Form, Reviews_Form
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from counter.models import Menu_items, Password
from django.db.models import Sum
# Create your views here.


def customer_home(request):
    #render customer home page
	if request.method == "POST":
		return HttpResponseRedirect(reverse('customer_details'))
	return render(request, 'customer/customer_home.html')

class customer_details(TemplateView):
	template_name='customer/customer_details.html'

	def get(self, request):
		form = Customer_Details_Form()
		return render(request, self.template_name, {'form':form})
	
	def post(self, request):
		form = Customer_Details_Form(request.POST)
		table = request.POST.get('table_no')
		name = request.POST.get('name')
		mobile_no = request.POST.get('mobile_no')
		request.session['table'] = table
		if form.is_valid():
			form.save()
			form = Customer_Details_Form()
			return HttpResponseRedirect(reverse('menu'))
		else:
			return render(request, self.template_name, {'form':form})


def menu (request):
	menu_items = Menu_items.objects.all()
	breakfast = menu_items.filter(category_name_id="1")
	lunch = menu_items.filter(category_name_id="2")
	dinner = menu_items.filter(category_name_id="3")
	supper = menu_items.filter(category_name_id="4")
	drinks = menu_items.filter(category_name_id="5")
	table = request.session['table']
	if request.method == "POST":
		quantity = request.POST.get('quantity')
		name = request.POST.get('name')
		price = request.POST.get('price_per_item')
		total = int(price)*int(quantity)
		Table_Orders.objects.create(food=name, price=price, table_no=table, quantity=quantity, total=total)
		print("form saved successfully")
	return render(request, 'customer/menu.html', {'breakfast': breakfast, 'lunch': lunch, 'dinner': dinner, 'supper': supper, 'drinks': drinks})

def customer_review(request):
    	#render customer review page
		table = request.session['table']
		get_name = Customer_Details.objects.get(table_no=table)
		name = get_name.customer_name
		mobile_no = get_name.mobile_no
		if request.method == "POST":
			rate = request.POST.get('rate')
			comment = request.POST.get('comment')
			Reviews.objects.create(table_no=table, phone_no=mobile_no, name=name, rate=rate, comment=comment)
			
			#SEND TEXT MESSAGE TO CUSTOMER USING TWILIO SMS API
			get_name = Customer_Details.objects.get(table_no=table)
			mobile_no = get_name.mobile_no
			get_new_password = Password.objects.get(id='1')
			fial_new_password = get_new_password.password
			amount_raw = Table_Orders.objects.filter(table_no=table).aggregate(Sum('total'))['total__sum']
			amount = str(amount_raw)
			account_sid = 'ACe2762dd9481b4c47b32e169697619f47'
			auth_token = 'b250c3f3d686751c43838a57b29953e1'
			client = Client(account_sid, auth_token)
			message = client.messages.create(
				to=mobile_no, from_="+12565008785", body="\n WI-FI Password: "+fial_new_password+".\nTOTAL AMOUNT: "+amount+"\nThank You for being our loyal Customer.\nWelcome!!",)
			print(message.sid)
			#END OF API
			
			print("form saved successfully")
			return HttpResponseRedirect(reverse('thank_customer'))
		return render(request, 'customer/customer_review.html')


def thank_customer(request):
    	#render thank customer page
	table = request.session['table']
	get_name = Customer_Details.objects.get(table_no=table)
	name = get_name.customer_name
	if request.method == "POST":
		Customer_Details.objects.filter(table_no=table).delete()
		del request.session['table']
		return HttpResponseRedirect(reverse('customer_home'))
	return render(request, 'customer/thank_customer.html', {'name':name})
