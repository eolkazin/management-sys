from django.urls import path
from app_sys import views

# Define as rotas de URL
urlpatterns = [
    path("", views.login_view, name="login"),  # Página de login
    path("cadastro/", views.cadastro_view, name="cadastro"),  # Página de cadastro
    path("hub/", views.hub_view, name="hub"),
    path(
        "logout/", views.logout_view, name="logout"
    ),  # Hub do sistema, onde o usuário será redirecionado após login
    path("estoque/", views.estoque_view, name="estoque"),  # Página de estoque
    path('estoque/deletar/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),
    path('produtos/', views.lista_produtos_view, name='lista_produtos'),
]
