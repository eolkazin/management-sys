from django.db import models


### Modelo de usuário com campos de username e password ###
class Usuario(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Nome de usuário único
    password = models.CharField(max_length=128)  # Senha do usuário
