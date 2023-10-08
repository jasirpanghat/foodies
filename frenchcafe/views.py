from django.shortcuts import render,redirect
from .models import Customer,log
from django.http import HttpResponse

# Create your views here.


def index(request):
    
    
    return render(request, 'index.html')
def register(request):

    if request.method == "POST":
        data=Customer()
        data.Customer_name=request.POST['cust_name']
        data.Customer_email=request.POST['cust_mail']
        data.Customer_city=request.POST['cust_city']
        data.Customer_country=request.POST['cust_country']


        log_data=log()
        log_data.email=request.POST['cust_mail']
        log_data.password=request.POST['cust_password']
        log_data.status=True
        
        log_data.save()

        data.Log_id=log.objects.last()
        #data=Customer(Customer_name=Customer_name,Customer_email=Customer_email,Customer_city=Customer_city,Customer_country=Customer_country)
        data.save()
  

    return render(request,'index.html')

def cust_login(request):

      

    return render(request,'index.html')



