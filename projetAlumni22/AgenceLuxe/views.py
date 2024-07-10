from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import *
from rest_framework.decorators import api_view
import json
from django.core.paginator import Paginator
from .serializers import *


def acceuil(request):
    
   
    return render(request, 'home.html')


def add_employee(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        date_nais = request.POST.get('date_nais')
        tel = request.POST.get('tel')
        date_empl = request.POST.get('date_empl')
        poste = request.POST.get('poste')
        
        Employe.objects.create(
            nom=nom,
            prenom=prenom,
            date_nais=date_nais,
            tel=tel,
            date_empl=date_empl,
            poste=poste
        )
        
        messages.success(request, "Employee added successfully!")
        return redirect('liste_employee')
    
    return render(request, 'add_employee.html')

def edit_employee(request, id):
    employee = get_object_or_404(Employe, id=id)
    
    if request.method == "POST":
        employee.nom = request.POST.get('nom')
        employee.prenom = request.POST.get('prenom')
        employee.date_nais = request.POST.get('date_nais')
        employee.tel = request.POST.get('tel')
        employee.date_empl = request.POST.get('date_empl')
        employee.poste = request.POST.get('poste')
        employee.save()
        
        messages.success(request, "Employee updated successfully!")
        return redirect('liste_employee')
    
    return render(request, 'edit_employee.html', {'employee': employee})

def delete_employee(request, id):
    employee = get_object_or_404(Employe, id=id)
    employee.delete()
    
    messages.success(request, "Employee deleted successfully!")
    return redirect('employee_list')

def employee_list(request):
    employees = Employe.objects.all()
    paginator = Paginator(employees, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'employee_list.html', {'page_obj': page_obj})

def view_employee(request, id):
    employee = get_object_or_404(Employe, id=id)
    return render(request, 'view_employee.html', {'employee': employee})

            
 