# -*- encoding: utf-8 -*-


from email.policy import default
import numbers
from unicodedata import numeric
from django.db import models
from django.contrib.auth.models import User


# Create your models here.db
class Voluntari (models.Model):
    GENDER=(
        ('Masculin', 'Masculin'),
        ('Feminin', 'Feminin'),
    )
    AN = (
        ('Anul I', 'Anul I'),
        ('Anul II', 'Anul II'),
        ('Anul III', 'Anul III'),
        ('Anul IV', 'Anul IV'),
        ('Anul V', 'Anul V'),
        ('Anul VI', 'Anul VI'),
     )
    
    id = models.BigAutoField(primary_key=True)
    nume = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField('Nume',max_length=200, null=True)
    last_name = models.CharField('Prenume',max_length=200, null=True)
    data = models.DateField('Data Nasterii', null=True)
    mail = models.EmailField('Email',null=True)
    phone = models.CharField('Nr. Telefon',max_length=200, null=True)
    gender= models.CharField('Sex',max_length=200, null=True, choices=GENDER)
    adress = models.CharField('Adresă',max_length=200, null=True)
    nr = models.CharField(max_length=200, null=True)
    city = models.CharField('Oras',max_length=200, null=True)
    judet = models.CharField('Judet',max_length=200, null=True)
    country = models.CharField('Tara',max_length=200, null=True)
    Facultate = models.CharField(max_length=200, null=True)
    specializare = models.CharField('Specializare',max_length=200, null=True)
    an= models.CharField('Anul de studiu',max_length=200, null=True, choices=AN)
    picture = models.ImageField(upload_to='djangouploads/files/covers', height_field=None, width_field=None, max_length=100)
    social = models.URLField('Adresa Facebook', null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Eveniment (models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('Activitate',max_length=200, null=True)
    locate = models.CharField('Locatie', max_length=200, null=True)
    data = models.DateTimeField('Data si ora', null=True)
    timp = models.FloatField('Durata',null=True)
    coord = models.ForeignKey(Voluntari, null=True, on_delete=models.CASCADE)
    descriere = models.TextField('Descriere', null=True,  blank=True)

    def __str__(self):
        return self.name