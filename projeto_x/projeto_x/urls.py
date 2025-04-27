from django.urls import path
from app_sys import views

# Define as rotas de URL
urlpatterns = [
    path("", views.login_view, name="login"),  # Página de login
    path("cadastro/", views.cadastro_view, name="cadastro"),
    path("hub/", views.hub_view, name="hub"),  # hub do sistema
]
