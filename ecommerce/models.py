from django.db import models
# Create your models here.
class User(models.Model):
    companyName = models.CharField(max_length=20)
    ownerName = models.CharField(max_length=20)
    rollNo = models.CharField(max_length=10)
    ownerEmail = models.EmailField()
    accessCode = models.CharField(max_length=6)
    
class Product(models.Model):
    productname = models.CharField(max_length=50, unique=True)
    price = models.CharField (max_length=8)
    rating = models.DecimalField(max_digits = 4,decimal_places=2)
    discount = models.DecimalField(max_digits= 2,decimal_places=2)
    availability = models.CharField(max_length=20)
    
