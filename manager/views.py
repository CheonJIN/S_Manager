from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Company, License, TechnicalSupport
from .forms import CustomerForm, CompanyForm, LicenseForm, TechnicalForm


# Create your views here.
def home(request):
    return render(request, 'manager/home.html', {}) 


def login(request):
    return render(request, 'registration/login.html', {})


def customer_list(request):
    customers = Customer.objects.order_by('name')
    
    return render(request, 'manager/customer_list.html', {'customers': customers})


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    
    return render(request, 'manager/customer_detail.html', {'customer': customer})


def customer_new(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            #customer.author = request.user
            customer.save()
            
            return redirect('customer_list')
        
    else:
        form = CustomerForm()
            
    return render(request, 'manager/customer_edit.html', {'form': form})


def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
        
    return render(request, 'manager/customer_edit.html', {'form': form})


def customer_remove(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    
    return redirect('customer_list')
    

def company_list(request):
    company = Company.objects.order_by('name')
    
    return render(request, 'manager/company_list.html', {'company': company})


def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    
    return render(request, 'manager/company_detail.html', {'company': company})


def company_new(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            #customer.author = request.user
            company.save()
            
            return redirect('company_list')
        
    else:
        form = CompanyForm()
            
    return render(request, 'manager/company_edit.html', {'form': form})


def company_edit(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            company = form.save(commit=False)
            company.save()
            
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)
        
    return render(request, 'manager/company_edit.html', {'form': form})


def company_remove(request, pk):
    company = get_object_or_404(Company, pk=pk)
    company.delete()
    
    return redirect('company_list')         
        
        
def license_list(request):
    licenses = License.objects.order_by('company')
    
    return render(request, 'manager/license_list.html', {'licenses': licenses})


def license_detail(request, pk):
    lic = get_object_or_404(License, pk=pk)
    return render(request, 'manager/license_detail.html', {'lic': lic})


def license_new(request):
    if request.method == "POST":
        form = LicenseForm(request.POST)
        if form.is_valid():
            lic = form.save(commit=False)
            lic.save()
            
            return redirect('license_list')
        
    else:
        form = LicenseForm()
            
    return render(request, 'manager/license_edit.html', {'form': form})


def license_edit(request, pk):
    lic = get_object_or_404(License, pk=pk)
    if request.method == "POST":
        form = LicenseForm(request.POST, instance=lic)
        if form.is_valid():
            lic = form.save(commit=False)
            lic.save()
            
            return redirect('license_list')
    else:
        form = LicenseForm(instance=lic)
        
    return render(request, 'manager/license_edit.html', {'form': form})


def license_remove(request, pk):
    lic = get_object_or_404(License, pk=pk)
    lic.delete()
    
    return redirect('license_list')


def technical_list(request):
    techs = TechnicalSupport.objects.order_by('support_date')
    
    return render(request, 'manager/technical_list.html', {'techs': techs})


def technical_new(request):
    if request.method == "POST":
        form = TechnicalForm(request.POST)
        if form.is_valid():
            tech = form.save(commit=False)
            tech.save()
            
            return redirect('technical_list')
    else:
        form = TechnicalForm()
    
    return render(request, 'manager/technical_edit.html', {'form': form})


def technical_edit(request, pk):
    tech = get_object_or_404(TechnicalSupport, pk=pk)
    if request.method == "POST":
        form = TechnicalForm(request.POST)
        if form.is_valid():
            tech = form.save(commit=False)
            tech.save()
            
            return redirect('technical_list')
    else:
        form = TechnicalForm()
    
    return render(request, 'manager/technical_edit.html', {'form': form})
