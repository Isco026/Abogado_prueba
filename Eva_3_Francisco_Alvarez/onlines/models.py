from django.db import models

# Create your models here.
class Preguntas(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_consulta = models.CharField(max_length=50)
    codigo_respuesta = models.CharField(max_length=50)
    cliente = models.CharField(max_length=50)
    consulta = models.CharField(max_length=50)

class Respuesta(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_consulta = models.CharField(max_length=50)
    codigo_respuesta = models.CharField(max_length=50)
    abogado = models.CharField(max_length=50)
    respuesta = models.CharField(max_length=50)

