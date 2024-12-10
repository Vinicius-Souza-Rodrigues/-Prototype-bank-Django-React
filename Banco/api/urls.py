from django.urls import path
from .views import UsuarioView #mudar dps para register

urlpatterns = [
    path('register', UsuarioView.as_view()),
]
