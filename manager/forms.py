'''
Created on 2019. 9. 23.

@author: jhcheon
'''
from django import forms
from .models import Customer, Company
from django.forms.fields import ChoiceField


class CustomerForm(forms.ModelForm):
#     def __init__(self, *args, **kw):
#         super(CustomerForm, self).__init__(*args, **kw)
#         self.fields.keyOrder = [
#              'name', 'rank', 'company', 'department', 'mobile', 'telecom', 'email', 'enrolled_date'   
#             ]
    
    class Meta:
        model = Customer
        fields = ('name', 'rank', 'company', 'department', 'mobile', 'telecom', 'email', 'enrolled_date',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'rank': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'telecom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'enrolled_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'manager', 'regional_office', 'enrolled_date',)
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'manager': forms.TextInput(attrs={'class': 'form-control'}),
#             #'regional_office': forms.CharField(choices=[('SEOUL', 'Seoul'), ('DAEJEAN', 'Daejean'), ('BUSAN', 'Busan')]),
#             #'regional_office': ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), required=True),
#             'enrolled_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
#         }