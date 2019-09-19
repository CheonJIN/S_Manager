from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Customar(models.Model):
    name = models.CharField(max_length=20)
    rank = models.CharField(max_length=20)
    company = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    telecom = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    enrolled_date = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.name