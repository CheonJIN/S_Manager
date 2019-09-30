'''
Created on 2019. 9. 23.

@author: jhcheon
'''
from django import forms
from .models import Customer, Company, License


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'rank', 'company', 'department', 'mobile', 'telecom', 'email', 'enrolled_date',)
        widgets = {
            'enrolled_date': forms.DateTimeInput(attrs={'type': 'date'}),
        }


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'manager', 'regional_office', 'enrolled_date',)
        widgets = {
            'enrolled_date': forms.DateTimeInput(attrs={'type': 'date'}),
        }


class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = ('company', 'ip', 'host', 'lum_target', 'dsls_target', 'count', 'module', 'memo', 'explaration_date',)
        widgets = {
            'explaration_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
        
        
        
        
