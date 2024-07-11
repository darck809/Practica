from django.db import models
#aqui se crea las tablas de la base de datos
# Create your models here.
class Project(models.Model):
    name: models.CharField(max_length=200)
    firstname = models.CharField(max_length=255)
