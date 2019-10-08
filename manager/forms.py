'''
Created on 2019. 9. 23.

@author: jhcheon
'''
from django import forms
from .models import Customer, Company, License, TechnicalSupport
from django.forms.widgets import Textarea
from django.forms.fields import CharField


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
            'explaration_date': forms.DateInput(attrs={'type': 'date', 'style': 'width: 100%'}),
            'ip': forms.TextInput(attrs={'style': 'width: 100%'}),
            'host': forms.TextInput(attrs={'style': 'width: 100%'}),
            'lum_target': forms.TextInput(attrs={'style': 'width: 100%'}),
            'dsls_target': forms.TextInput(attrs={'style': 'width: 100%'}),
            'module': forms.TextInput(attrs={'style': 'width: 100%'}),
            'memo': forms.TextInput(attrs={'style': 'width: 100%'}),
            'count': forms.NumberInput(attrs={'style': 'width: 100%'}),
        }
        

class TechnicalForm(forms.ModelForm):
    class Meta:
        model = TechnicalSupport
        fields = ('company', 'customer_name', 'support_staff', 'support_date', 'support_type', 'requestment', 'answer',)
        widgets = {
            'support_date': forms.DateInput(attrs={'type': 'date', 'style': 'width: 100%'}),
            'requestment': Textarea(attrs={'style': 'width: 100%'}),
            'answer': Textarea(attrs={'style': 'width: 100%'}),
            'customer_name': forms.TextInput(attrs={'style': 'width: 100%'}),
        }
    