<<<<<<< HEAD
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password_confirmation = forms.CharField(widget=forms.PasswordInput, label='Password confirmation')

    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        }

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if password != password_confirmation:
            raise ValidationError("Passwords do not match.")
        return password_confirmation

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")
        return username
=======

from django import forms
from .models import *


class EnregistreUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nom', 'prenom', 'tel', 'imag']
        widgets = {
            'nom' :forms.TextInput(attrs = {'class': "form-control"}),
            'prenom' : forms.TextInput(attrs = {'class': "form-control"}),
            'tel' :forms.TextInput(attrs = {'class': "form-control"}),
            'imag' : forms.TextInput(attrs = {'class': "form-control"}),
        }
        
class EmployesForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['nom', 'prenom', 'tel', 'imag']
        widgets = {
            'nom' :forms.TextInput(attrs = {'class': "form-control"}),
            'prenom' : forms.TextInput(attrs = {'class': "form-control"}),
            'tel' :forms.TextInput(attrs = {'class': "form-control"}),
            'imag' : forms.TextInput(attrs = {'class': "form-control"}),
        }
>>>>>>> 286a8375ba18b5139a39fb333bde7a1c72e528c1
