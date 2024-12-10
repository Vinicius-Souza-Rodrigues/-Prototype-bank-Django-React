from django.shortcuts import render
from rest_framework import generics
from .serializers import UsuarioSerializer
from django.http import HttpResponse
from .models import Usuario

#register
class UsuarioView(generics.CreateAPIView):
    queryset = Usuario.objects.all() #oq vou retornar esta decidido aq
    serializer_class = UsuarioSerializer
