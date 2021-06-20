from django.db import models
from django_mysql.models import ListTextField
#A clas for the list field


   
# Create your models here.

class hospital(models.Model):
    id=models.IntegerField(null=False, primary_key=True)
    name=models.CharField(max_length=50, unique=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=150)
    type=models.CharField(max_length=150)
    Ratings=models.IntegerField(null=False)
    diseases=ListTextField(
        base_field=models.CharField(max_length=15, unique=True),
        size=150, default='hello'
    )
    treatments=ListTextField(
        base_field=models.CharField(max_length=15, unique=True),
        size=150, default='Hello'
    )
    noOfDoctors=models.IntegerField(null=False)
    noOfBeds=models.IntegerField(null=False)
    link=models.CharField(max_length=150, unique=True)
    image = models.CharField(max_length=450, unique=True, default='image')
    pincode=models.CharField(max_length=10, default='000000')
    latitude=models.CharField(max_length=10, default='0.0')
    longitude=models.CharField(max_length=10, default='0.0')









