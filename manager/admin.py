from django.contrib import admin
from .models import Customer, Company, License, TechnicalSupport

# Register your models here.
admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(License)
admin.site.register(TechnicalSupport)