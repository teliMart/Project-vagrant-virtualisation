from django import views
from django.urls import path,include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', accueil, name='employee'),
    path('employee/detail/<int:id>/', view_employee, name='view_employee'),
    path('addemployee/', add_employee, name='add_employee'),
    path('editemployee/<int:id>/', edit_employee, name='edit_employee'),
    path('listemployee/', employee_list, name='liste_employee'),
    path('deleteemployee/<int:id>/', delete_employee, name='delete_employee'),
    path('register/', register, name='register'),
    path('', connecter, name='login'),
    path('deconnecter',deconnecter, name='logout'),
    path('profile/', view_employee_profile, name='view_employee_profile'),
     path('employee/maj/<int:employee_id>/', maj_employee, name='maj_employee'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
