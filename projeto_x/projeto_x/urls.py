from django.urls import path
from app_sys import views

# Define as rotas de URL
urlpatterns = [
    path("", views.login_view, name="login"),  # Página de login
    path("cadastro/", views.cadastro_view, name="cadastro"),  # Página de cadastro
    path("hub/", views.hub_view, name="hub"),  # Página do hub, após login
    path(
        "logout/", views.logout_view, name="logout"
    ),  # Desconecta o usuário e redireciona para login
    path("estoque/", views.estoque_view, name="estoque"),  # Página de estoque
    path(
        "estoque/deletar/<int:produto_id>/",
        views.deletar_produto,
        name="deletar_produto",
    ),  # Deleta um produto do estoque
    path(
        "produtos/", views.lista_produtos_view, name="lista_produtos"
    ),  # Lista todos os produtos
    path(
        "cad_cliente/", views.cad_cliente_view, name="cad_cliente"
    ),  # Página de cadastro de cliente
    path(
        "lista_cliente/", views.lista_clientes_view, name="lista_cliente"
    ),  # Lista todos os clientes
]
