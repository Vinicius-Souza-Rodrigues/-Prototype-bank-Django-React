from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer

class RegisterView(APIView):
    def post(self, request):
        data = request.data

        if User.objects.filter(username=data.get('username')).exists():
            return Response({'error': 'Já existe um usuário com esse nome.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password')
        )

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            auth_login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Credenciais inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)

class PlataformaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response({
            'message': f'Bem-vindo à plataforma, {user.username}!',
            'user': serializer.data
        }, status=status.HTTP_200_OK)
