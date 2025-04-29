from django.db import models


### Modelo de usuário com campos de username e password ###
class Usuario(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Nome de usuário único
    password = models.CharField(max_length=128)  # Senha do usuário


### Modelo de produto com diversos campos de informações do produto ###
class Produto(models.Model):
    nome = models.CharField(max_length=255)  # Nome do produto
    descricao = models.TextField()  # Descrição do produto
    categoria = models.CharField(max_length=100)  # Categoria do produto
    fornecedor = models.CharField(max_length=100)  # Fornecedor do produto
    custo_unitario = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # Custo unitário do produto
    preco_venda = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # Preço de venda do produto
    quantidade = models.IntegerField()  # Quantidade do produto em estoque
    localizacao = models.CharField(max_length=100)  # Localização no estoque
    data_validade = models.DateField(
        null=True, blank=True
    )  # Data de validade do produto (opcional)

    def __str__(self):
        return self.nome


### Modelo de cliente com dados pessoais e de contato ###
class Cliente(models.Model):
    nome = models.CharField(max_length=255)  # Nome do cliente
    email = models.EmailField()  # Email do cliente
    telefone = models.CharField(max_length=20)  # Telefone do cliente
    endereco = models.CharField(max_length=255)  # Endereço do cliente
    cidade = models.CharField(max_length=100)  # Cidade do cliente
    estado = models.CharField(max_length=50)  # Estado do cliente
    cpf = models.CharField(max_length=14, unique=True)  # CPF único do cliente
    data_nascimento = models.DateField(
        null=True, blank=True
    )  # Data de nascimento do cliente (opcional)

    def __str__(self):
        return self.nome
