from django.contrib.auth.models import AbstractUser
from django.db import models
from .validate import validate_CPF, validate_Telefone


class User(AbstractUser):
	cpf = models.CharField(max_length=11, blank=True, validators=[validate_CPF], verbose_name='CPF')
	phone = models.CharField(max_length=11, blank=True, validators=[validate_Telefone], verbose_name='Telefone')
