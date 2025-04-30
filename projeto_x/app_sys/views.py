from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password
from .models import Usuario, Produto, Cliente


### Login ###
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        usuario = Usuario.objects.filter(username=username).first()
        if usuario and check_password(password, usuario.password):
            request.session["usuario_id"] = usuario.id
            return redirect("hub")

        messages.error(request, "Usuário ou senha inválidos.")
        return redirect("login")

    return render(request, "login/login.html")


### Cadastro de Usuário ###
def cadastro_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        senha1 = request.POST.get("password1")
        senha2 = request.POST.get("password2")

        if senha1 != senha2:
            messages.error(request, "As senhas não coincidem.")
            return redirect("cadastro")

        if Usuario.objects.filter(username=username).exists():
            messages.error(request, "Usuário já existe.")
            return redirect("cadastro")

        Usuario.objects.create(username=username, password=make_password(senha1))
        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect("login")

    return render(request, "login/cadastro.html")


### Hub ###
def hub_view(request):
    usuario_id = request.session.get("usuario_id")
    if not usuario_id:
        return redirect("login")

    usuario = Usuario.objects.filter(id=usuario_id).first()
    if not usuario:
        return redirect("login")

    return render(request, "hub/hub.html", {"usuario": usuario})


### Logout ###
def logout_view(request):
    logout(request)
    return redirect("login")


### Estoque - Cadastro de Produto ###
def estoque_view(request):
    if request.method == "POST":
        campos = [
            "nome",
            "descricao",
            "categoria",
            "fornecedor",
            "custo_unitario",
            "preco_venda",
            "quantidade",
            "localizacao",
            "data_validade",
        ]
        dados = {campo: request.POST.get(campo) for campo in campos}
        if not dados.get("data_validade"):
            dados["data_validade"] = None

        Produto.objects.create(**dados)
        return redirect("estoque")

    produtos = Produto.objects.all()
    return render(request, "estoque/estoque.html", {"produtos": produtos})


### Estoque - Deletar Produto ###
def deletar_produto(request, produto_id):
    if request.method == "POST":
        produto = get_object_or_404(Produto, id=produto_id)
        produto.delete()
    return redirect("estoque")


### Estoque - Lista de Produtos ###
def lista_produtos_view(request):
    produtos = Produto.objects.all()
    return render(request, "estoque/lista_produtos.html", {"produtos": produtos})


### Cadastro de Cliente ###
def cad_cliente_view(request):
    if request.method == "POST":
        campos = [
            "nome",
            "email",
            "telefone",
            "endereco",
            "cidade",
            "estado",
            "cpf",
            "data_nascimento",
        ]
        dados = {campo: request.POST.get(campo) for campo in campos}
        if not dados.get("data_nascimento"):
            dados["data_nascimento"] = None

        Cliente.objects.create(**dados)
        return redirect("cad_cliente")

    return render(request, "cad_cliente/cad_cliente.html")


### Lista de Clientes ###
def lista_clientes_view(request):
    clientes = Cliente.objects.all()
    return render(request, "cad_cliente/lista_cliente.html", {"clientes": clientes})


### Dashboard ###
def dashboard_view(request):
    produtos = Produto.objects.all()
    clientes = Cliente.objects.all()

    receita = sum(prod.preco_venda * prod.quantidade for prod in produtos)
    despesas = sum(prod.custo_unitario * prod.quantidade for prod in produtos)

    context = {
        "produtos": produtos,
        "clientes": clientes,
        "receita": receita,
        "despesas": despesas,
        "novos_clientes": clientes.count(),
        "meta": 72,
    }
    return render(request, "dashboard/dashboard.html", context)
