from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import *
<<<<<<< HEAD
from rest_framework.decorators import api_view # type: ignore
import json
from django.core.paginator import Paginator
from .serializers import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
=======
from rest_framework.decorators import api_view
import json
from django.core.paginator import Paginator
from .serializers import *
>>>>>>> 286a8375ba18b5139a39fb333bde7a1c72e528c1


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
<<<<<<< HEAD
    return redirect('liste_employee')
=======
    return redirect('employee_list')
>>>>>>> 286a8375ba18b5139a39fb333bde7a1c72e528c1

def employee_list(request):
    employees = Employe.objects.all()
    paginator = Paginator(employees, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'employee_list.html', {'page_obj': page_obj})

def view_employee(request, id):
    employee = get_object_or_404(Employe, id=id)
    return render(request, 'view_employee.html', {'employee': employee})

<<<<<<< HEAD



from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Création de l'utilisateur
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirection vers la page de connexion après l'inscription
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})





def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('employee')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

=======
>>>>>>> 286a8375ba18b5139a39fb333bde7a1c72e528c1
            
 