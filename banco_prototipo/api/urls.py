from django.urls import path
from .views import RegisterView, LoginView, PlataformaView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('plataforma/', PlataformaView.as_view(), name='plataforma')
]
