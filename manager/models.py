from django.db import models
from django.utils import timezone
from django import forms


AREA_CHOICES = [
    ('SEOUL', 'Seoul'),
    ('DAEJEAN', 'Daejean'),
    ('BUSAN', 'Busan'),
    ('CHANGWON', 'Changwon'),
    ('GWHANGJU', 'Gwhanju'),
]


# Create your models here.
class Customer(models.Model):
    #author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    rank = models.CharField(max_length=20)
    company = models.CharField(max_length=30)
    #company = models.ForeignKey('manager.Company', related_name='customers', on_delete=models.CASCADE)
    department = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    telecom = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    enrolled_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    
    
class Company(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    manager = models.CharField(max_length=20)
    #regional_office = models.CharField(max_length=10)
    regional_office = models.CharField(max_length=15, choices=AREA_CHOICES)
    enrolled_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    