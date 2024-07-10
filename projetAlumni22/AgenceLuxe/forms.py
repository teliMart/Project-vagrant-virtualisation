
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
