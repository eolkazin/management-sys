from django.urls import path
from app_sys import views

urlpatterns = [
    ### login e autenticação ###
    path("", views.login_view, name="login"),  # ### exibe tela de login ###
    path("cadastro/", views.cadastro_view, name="cadastro"),  # ### tela de cadastro ###
    path("logout/", views.logout_view, name="logout"),  # ### encerra sessão ###
    ### pós-login / hub ###
    path("hub/", views.hub_view, name="hub"),  # ### dashboard inicial após login ###
    ### dashboard geral ###
    path(
        "dashboard/", views.dashboard_view, name="dashboard"
    ),  # ### visão geral dos dados ###
    ### estoque ###
    path(
        "estoque/", views.estoque_view, name="estoque"
    ),  # ### cadastro e listagem de produtos ###
    path(
        "estoque/deletar/<int:produto_id>/",
        views.deletar_produto,
        name="deletar_produto",
    ),  # ### deleta produto do estoque ###
    path(
        "produtos/", views.lista_produtos_view, name="lista_produtos"
    ),  # ### lista todos os produtos ###
    ### clientes ###
    path(
        "cad_cliente/", views.cad_cliente_view, name="cad_cliente"
    ),  # ### cadastro de cliente ###
    path(
        "lista_cliente/", views.lista_clientes_view, name="lista_cliente"
    ),  # ### lista todos os clientes ###
]
