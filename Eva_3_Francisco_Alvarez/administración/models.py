from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    tipo_usuario= models.CharField(max_length=25)