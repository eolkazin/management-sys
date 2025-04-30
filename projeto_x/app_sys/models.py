from django.db import models


### modelo de usuário ###
class Usuario(models.Model):
    username = models.CharField(
        max_length=150, unique=True
    )  # ### nome de usuário único ###
    password = models.CharField(max_length=128)  # ### senha hash do usuário ###

    def __str__(self):
        return self.username


### modelo de produto ###
class Produto(models.Model):
    nome = models.CharField(max_length=255)  # ### nome do produto ###
    descricao = models.TextField()  # ### descrição detalhada ###
    categoria = models.CharField(max_length=100)  # ### tipo/categoria ###
    fornecedor = models.CharField(max_length=100)  # ### nome do fornecedor ###
    custo_unitario = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # ### custo por unidade ###
    preco_venda = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # ### preço de venda ###
    quantidade = models.IntegerField()  # ### estoque atual ###
    localizacao = models.CharField(max_length=100)  # ### onde tá no estoque ###
    data_validade = models.DateField(
        null=True, blank=True
    )  # ### validade (opcional) ###

    def __str__(self):
        return self.nome


### modelo de cliente ###
class Cliente(models.Model):
    nome = models.CharField(max_length=255)  # ### nome completo ###
    email = models.EmailField()  # ### e-mail ###
    telefone = models.CharField(max_length=20)  # ### número de contato ###
    endereco = models.CharField(max_length=255)  # ### endereço completo ###
    cidade = models.CharField(max_length=100)  # ### cidade ###
    estado = models.CharField(max_length=50)  # ### estado ###
    cpf = models.CharField(max_length=14, unique=True)  # ### CPF (único) ###
    data_nascimento = models.DateField(
        null=True, blank=True
    )  # ### nascimento (opcional) ###

    def __str__(self):
        return self.nome
