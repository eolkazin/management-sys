from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Produto, Cliente
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.contrib.auth import logout


### Exibe a página de login e valida as credenciais ###
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            usuario = Usuario.objects.get(username=username)
            if check_password(password, usuario.password):
                # Senha correta, cria a sessão do usuário
                request.session["usuario_id"] = usuario.id
                return redirect("hub")
            else:
                # Senha incorreta
                messages.error(request, "Usuário ou senha inválidos.")
                return redirect("login")
        except Usuario.DoesNotExist:
            # Usuário não encontrado
            messages.error(request, "Usuário ou senha inválidos.")
            return redirect("login")

    return render(request, "login/login.html")


### Exibe a página de cadastro e realiza a criação de um novo usuário ###
def cadastro_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            # Se as senhas não coincidirem, exibe mensagem de erro
            messages.error(request, "As senhas não coincidem.")
            return redirect("cadastro")

        if not Usuario.objects.filter(username=username).exists():
            # Se o usuário não existir, cria um novo usuário com senha criptografada
            hashed_password = make_password(password1)
            Usuario.objects.create(username=username, password=hashed_password)
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect("login")
        else:
            # Se o usuário já existir, exibe mensagem de erro
            messages.error(request, "Usuário já existe.")
            return redirect("cadastro")

    return render(request, "login/cadastro.html")


### Exibe a página do hub para o usuário logado ###
def hub_view(request):
    # Verifica se o usuário está logado
    usuario_id = request.session.get("usuario_id")
    if usuario_id:
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            return render(request, "hub/hub.html", {"usuario": usuario})
        except Usuario.DoesNotExist:
            return redirect("login")  # Caso o usuário não exista mais
    else:
        return redirect("login")  # Se o usuário não estiver logado


### Desconecta o usuário e redireciona para a página de login ###
def logout_view(request):
    logout(request)  # Desconecta o usuário
    return redirect("login")  # Redireciona para a página de login


### Exibe e processa a página de estoque (adicionar produtos) ###
def estoque_view(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        categoria = request.POST.get("categoria")
        fornecedor = request.POST.get("fornecedor")
        custo_unitario = request.POST.get("custo_unitario")
        preco_venda = request.POST.get("preco_venda")
        quantidade = request.POST.get("quantidade")
        localizacao = request.POST.get("localizacao")
        data_validade = request.POST.get("data_validade")

        Produto.objects.create(
            nome=nome,
            descricao=descricao,
            categoria=categoria,
            fornecedor=fornecedor,
            custo_unitario=custo_unitario,
            preco_venda=preco_venda,
            quantidade=quantidade,
            localizacao=localizacao,
            data_validade=data_validade if data_validade else None,
        )
        return redirect("estoque")  # Reload na página pra ver o novo produto
    produtos = Produto.objects.all()
    return render(request, "estoque/estoque.html", {"produtos": produtos})


### Deleta um produto do estoque ###
def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == "POST":
        produto.delete()
        return redirect("estoque")


### Lista todos os produtos no estoque ###
def lista_produtos_view(request):
    produtos = Produto.objects.all()  # Pega todos os produtos
    return render(request, "estoque/lista_produtos.html", {"produtos": produtos})


### Exibe e processa a página de cadastro de clientes ###
def cad_cliente_view(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        endereco = request.POST.get("endereco")
        cidade = request.POST.get("cidade")
        estado = request.POST.get("estado")
        cpf = request.POST.get("cpf")
        data_nascimento = request.POST.get("data_nascimento")

        Cliente.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            endereco=endereco,
            cidade=cidade,
            estado=estado,
            cpf=cpf,
            data_nascimento=data_nascimento if data_nascimento else None,
        )
        return redirect("cad_cliente")  # Pode mudar o redirect se quiser

    return render(request, "cad_cliente/cad_cliente.html")


### Lista todos os clientes cadastrados ###
def lista_clientes_view(request):
    clientes = Cliente.objects.all()
    return render(request, "cad_cliente/lista_cliente.html", {"clientes": clientes})
