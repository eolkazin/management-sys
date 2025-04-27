from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.hashers import check_password
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

    return render(request, "login.html")


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

    return render(request, "cadastro.html")


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


def estoque_view(request):
    return render(request, "hub/estoque/estoque.html")  # Renderiza a página de estoque
