from django.http import HttpResponse
from django.shortcuts import render
from dbapp.models import Customer,Authentication,Payment
# Create your views here.
def get_customers(request):
    customers = Customer.objects.all()
    return render(request,'get_customers.html',{'customers':customers})

def get_authentication(request):
    authentication = Authentication.objects.all()
    return render(request,'get_authentication.html',{'authentication':authentication})
def get_payment(request):
    payment = Payment.objects.all()
    return render(request,'get_payment.html',{'payment':payment})

