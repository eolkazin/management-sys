from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth.hashers import make_password
from django.contrib import messages


### Exibe a página de login e valida as credenciais ###
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            # Tenta encontrar o usuário com as credenciais fornecidas
            usuario = Usuario.objects.get(username=username, password=password)
            request.session["usuario_id"] = usuario.id
            return redirect("home")
        except Usuario.DoesNotExist:
            # Se o usuário não for encontrado, exibe mensagem de erro
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
