from django.db import models
from django.contrib.auth.models import User



class Employe(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=50)
    date_nais = models.CharField(max_length=20) 
    tel = models.CharField(max_length=20)
    date_empl = models.CharField(max_length=20)
    photo = models.ImageField(verbose_name='photo de profile', default="image/person-circle.svg", upload_to='img_userProfile')
    POSTE_CHOICES = [
        ('manager', 'Manager'),
        ('developeur', 'Developeur'),
        ('designer', 'Designer'),
        ('analyste', 'Analyste'),
        ('secretaire', 'Secretaire'),
        ('vigile', 'Vigile'),
    ]
    poste = models.CharField(max_length=20, choices=POSTE_CHOICES)
    def __str__(self):
        return self.nom
    
    def photoUrl(self ):
        try:
            url=self.photo.url 
        except : 
            url="image/person-circle.svg"
        return url


