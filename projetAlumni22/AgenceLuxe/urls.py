from django import views
from django.urls import path,include
from .views import *


urlpatterns = [
    path('', acceuil, name='employee'),
    path('employee/detail/<int:id>/', view_employee, name='view_employee'),
    path('addemployee/', add_employee, name='add_employee'),
    path('editemployee/<int:id>/', edit_employee, name='edit_employee'),
    path('listemployee/', employee_list, name='liste_employee'),
    path('deleteemployee/<int:id>/', delete_employee, name='delete_employee'),
]
