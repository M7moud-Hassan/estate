from django.db import models

# Create your models here.
class Imported(models.Model):
    company_name=models.CharField(max_length=50,null=True,blank=True)
    phonesNumber=models.ManyToManyField('PhoneNumber',null=True,blank=True)
    website=models.CharField(max_length=200,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    address=models.CharField(max_length=300,null=True,blank=True)

class PhoneNumber(models.Model):
    phone_number=models.CharField(max_length=50,null=True,blank=True)
