from django.db import models



class Employe(models.Model):
    nom = models.CharField(max_length=20)
<<<<<<< HEAD
    prenom = models.CharField(max_length=50)
=======
    prenom = models.CharField(max_length=20)
>>>>>>> 286a8375ba18b5139a39fb333bde7a1c72e528c1
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


