
from django.shortcuts import render
from .models import Company, Employee, Device, CheckoutLog

def checkout(request):
    # Logic for checkout process
    return render(request, 'checkout.html')

def checkin(request):
    # Logic for check-in process
    return render(request, 'checkin.html')

def company_details(request, company_id):
    company = Company.objects.get(pk=company_id)
    employees = Employee.objects.filter(company=company)
    devices = Device.objects.filter(company=company)
    return render(request, 'company_details.html', {'company': company, 'employees': employees, 'devices': devices})
