from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import *
from rest_framework.decorators import api_view # type: ignore
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .serializers import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Count

def accueil(request):
    employes_par_poste = Employe.objects.values('poste').annotate(total=Count('poste')).order_by('poste')
    employees = Employe.objects.all()
    paginator = Paginator(employees, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Créer un dictionnaire avec le nombre d'employés par poste
    employes_count = {item['poste']: item['total'] for item in employes_par_poste}
    
    context = {
        'employes_count': employes_count,
        'page_obj': page_obj
    }
    
    return render(request, 'home.html', context)


def add_employee(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        date_nais = request.POST['date_nais']
        tel = request.POST['tel']
        date_empl = request.POST['date_empl']
        poste = request.POST['poste']
        photo = request.FILES.get('photo', 'image/person-circle.svg')  # Default image if no file uploaded

        # Créer l'utilisateur
        user = User.objects.create_user(username=username, email=email, password=password)

        # Créer l'employé
        Employe.objects.create(
            user_id=user,
            nom=nom,
            prenom=prenom,
            date_nais=date_nais,
            tel=tel,
            date_empl=date_empl,
            poste=poste,
            photo=photo
        ) 
        messages.success(request, "Employé ajouté avec succès!")
        return redirect('employee') 
        
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
    return redirect('liste_employee')

def employee_list(request):
    employees = Employe.objects.all()
    paginator = Paginator(employees, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'employee_list.html', {'page_obj': page_obj})

def view_employee(request, id):
    employee = get_object_or_404(Employe, id=id)
    return render(request, 'view_employee.html', {'employee': employee})




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


    
    
def inscrireuser(request):
     if request.method == 'POST':
         username = request.POST['username']
         lastname = request.POST['last_name']
         firstname = request.POST['first_name']
         email= request.POST['email']
         password = request.POST['password'] 
         if User.objects.filter(username=username).exists():
                messages.error(request,"Le INE que vous avez saisi existe déjà. Vous ne pouvez plus créer de compte avec le même INE ")
                return redirect('register')
         else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"L'adresse email que vous avez entré existe déjà ")
                    return redirect('register')
                else:
                    
                        mon_user = User.objects.create_user(username, email, password)
                        mon_user.first_name = firstname
                        mon_user.last_name = lastname
                        mon_user.save()
                        messages.success(request, 'votre compte a été crée avec succès')
                        return redirect('logins')
                  
     else:
         
        return render(request, 'register.html')
    
    
def connecter(request):
    if request.method == 'POST':
         username = request.POST['username'],
         passwor = request.POST['password'],
         use= authenticate(username=request.POST['username'], password=request.POST['password'])
         if use is not None:
             login(request, use)
             nom = User.id
             messages.success(request, 'Vous êtes connecté!!!!')
             return redirect('employee')
         else:
            messages.error(request,'Connection impossible')
            return redirect('login')
    return render(request, 'login.html')

def deconnecter(request):
    logout(request)
    messages.success(request, 'votre compte a été deconnecté')
    return redirect('login')       
 