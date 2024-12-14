from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated

class RegistroView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({"error": "Usuário já existe."}, status=HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return Response({"message": "Usuário cadastrado com sucesso!"}, status=HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return Response({"message": f"Bem-vindo, {user.username}!"}, status=HTTP_200_OK)
        else:
            return Response({"error": "Credenciais inválidas."}, status=HTTP_400_BAD_REQUEST)

class PlataformaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Você está autenticado na plataforma."}, status=HTTP_200_OK)
