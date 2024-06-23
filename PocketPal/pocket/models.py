from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=254,null=True)
    correo = models.EmailField(null=True)
    password = models.CharField(max_length=254,null=True)