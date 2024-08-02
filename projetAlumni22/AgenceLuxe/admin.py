from django.contrib import admin
from .models import Employe

@admin.register(Employe)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'tel', 'date_nais','date_empl')  


