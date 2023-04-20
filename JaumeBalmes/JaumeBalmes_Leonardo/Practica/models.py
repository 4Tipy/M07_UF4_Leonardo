from django.db import models

class Person(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50, default='')
    año = models.IntegerField()
    edad = models.PositiveIntegerField()
    email = models.EmailField()


