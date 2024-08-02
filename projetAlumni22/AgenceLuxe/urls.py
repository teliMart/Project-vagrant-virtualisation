from django import views
from django.urls import path,include
from .views import *


urlpatterns = [
<<<<<<< HEAD
    path('login/', acceuil, name='employee'),
=======
    path('', acceuil, name='employee'),
>>>>>>> 286a8375ba18b5139a39fb333bde7a1c72e528c1
    path('employee/detail/<int:id>/', view_employee, name='view_employee'),
    path('addemployee/', add_employee, name='add_employee'),
    path('editemployee/<int:id>/', edit_employee, name='edit_employee'),
    path('listemployee/', employee_list, name='liste_employee'),
    path('deleteemployee/<int:id>/', delete_employee, name='delete_employee'),
<<<<<<< HEAD
    path('register/', register, name='register'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

=======
>>>>>>> 286a8375ba18b5139a39fb333bde7a1c72e528c1
]
