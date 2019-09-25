from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Company
from .forms import CustomerForm, CompanyForm


# Create your views here.
def home(request):
    return render(request, 'manager/home.html', {}) 


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
        