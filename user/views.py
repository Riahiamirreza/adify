from django.contrib.auth import authenticate, login

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from user.serializers import UserSerializer
from user.models import User


class UserView(APIView):
    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            email = request.data.get('email')
            if username and password and email:
                user = User.objects.create_user(username=username, password=password, email=email)
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if (user := authenticate(request, username=username, password=password)) is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        login(request=request, user=user)
        return Response(status=status.HTTP_200_OK)
