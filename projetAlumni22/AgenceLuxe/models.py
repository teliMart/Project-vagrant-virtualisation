from django.db import models



class Employe(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=40)
    date_nais = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    date_empl = models.CharField(max_length=20)
    POSTE_CHOICES = [
        ('manager', 'Manager'),
        ('developer', 'Developer'),
        ('designer', 'Designer'),
        ('analyst', 'Analyst'),
    ]
    poste = models.CharField(max_length=20, choices=POSTE_CHOICES)


