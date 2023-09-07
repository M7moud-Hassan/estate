from django.db import models


# Create your models here.

class Engineers(models.Model):
    name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=10)
    graduation_year = models.IntegerField(max_length=4)
    phone_number = models.CharField(max_length=50)
