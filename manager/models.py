from django.db import models
from django.utils import timezone


AREA_CHOICES = [
    ('SEOUL', 'Seoul'),
    ('DAEJEON', 'Daejeon'),
    ('BUSAN', 'Busan'),
    ('CHANGWON', 'Changwon'),
    ('GWHANGJU', 'Gwhanju'),
]

SUPPORT_CHOICES = [
    ('INSIDE', 'Inside'),
    ('OUTSIDE', 'Outside'),
]


# Create your models here.
class Customer(models.Model):
    #author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    rank = models.CharField(max_length=20)
    #company = models.CharField(max_length=30)
    company = models.ForeignKey('manager.Company', related_name='customers', on_delete=models.CASCADE)
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
    

class License(models.Model):
    company = models.ForeignKey('manager.Company', related_name='licenses', on_delete=models.CASCADE)
    ip = models.CharField(max_length=20)
    host = models.CharField(max_length=20)
    lum_target = models.CharField(max_length=20)
    dsls_target = models.CharField(max_length=20)
    count = models.IntegerField()
    module = models.CharField(max_length=100)
    memo = models.CharField(max_length=200)
    explaration_date = models.DateField()
    
    
class TechnicalSupport(models.Model):
    support_staff = models.ForeignKey('auth.User', on_delete=models.CASCADE)    
    support_date = models.DateTimeField(default=timezone.now)
    support_type = models.CharField(max_length=15, choices=SUPPORT_CHOICES)
    company = models.ForeignKey('manager.Company', related_name='technicalSupport', on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=20)
    requestment = models.TextField()
    answer = models.TextField()
    
    
    
    