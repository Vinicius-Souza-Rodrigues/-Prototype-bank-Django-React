from rest_framework import serializers
from .models import Usuario

#register
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'username', 'email', 'cpf', 'password', 'saldo')
