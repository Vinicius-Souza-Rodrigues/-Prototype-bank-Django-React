from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    saldo = models.IntegerField(default=0)

