from django.db import models


# Create your models here.
class log(models.Model):
    
    log_id=models.AutoField(primary_key=True)
    email=models.CharField(max_length=60,unique=True)
    password=models.CharField(max_length=50)
    status=models.BooleanField(default=False)

     
class Customer(models.Model):
    Customer_id = models.AutoField(primary_key=True)
    Customer_name=models.CharField("name",max_length=200)
    
    Customer_email = models.EmailField("email",max_length=100,unique=True)
    Customer_city = models.CharField("city",max_length=15)
    Customer_country = models.CharField("country",max_length=300)
    Log_id=models.ForeignKey(log,on_delete=models.CASCADE)


    