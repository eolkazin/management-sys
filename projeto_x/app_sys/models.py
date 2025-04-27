from django.db import models

### Modelo de usuário com campos de username, password e tipo ###
class Usuario(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Nome de usuário único
    password = models.CharField(max_length=128)  # Senha do usuário
    tipo = models.CharField(
        max_length=50,
        choices=[('financeiro', 'Financeiro'), 
                 ('estoque', 'Estoque'),
                 ('dev', 'Desenvolvimento')],
        default='estoque'  # Define 'estoque' como valor padrão
    )

    def __str__(self):
        return self.username
