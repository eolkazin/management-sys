from django.db import models


### Modelo de usuário com campos de username e password ###
class Usuario(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Nome de usuário único
    password = models.CharField(max_length=128)  # Senha do usuário


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    categoria = models.CharField(max_length=100)
    fornecedor = models.CharField(max_length=100)
    custo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    localizacao = models.CharField(max_length=100)
    data_validade = models.DateField(null=True, blank=True)
    imagem = models.ImageField(upload_to="produtos/", null=True, blank=True)

    def __str__(self):
        return self.nome
