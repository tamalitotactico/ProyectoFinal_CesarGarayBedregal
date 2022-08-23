from datetime import datetime
from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=50)
    dni = models.PositiveIntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    birthdate = models.DateField()
    adress = models.CharField(max_length = 80)

class platillo(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)

class pedido(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.CharField(max_length=50)
    fecha = models.DateField()

