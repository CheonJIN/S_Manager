from django.contrib import admin
from .models import Customer, Company, License

# Register your models here.
admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(License)
