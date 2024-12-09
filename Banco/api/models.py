from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50, default='', unique=False)
    email = models.CharField(max_length=50, default='', unique=True)
    cpf = models.CharField(max_length=11, default='', unique=True)
    password = models.CharField(max_length=50, default='', unique=False)
    saldo = models.IntegerField(max_length=20, default='', unique=False)

