from django.db import models

class Person(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    año = models.IntegerField()



