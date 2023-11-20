from django.contrib.auth import authenticate, login

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from user.serializers import UserSerializer


class UserView(APIView):
    ...

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if (user := authenticate(request, username=username, password=password)) is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        login(request=request, user=user)
        return Response(status=status.HTTP_200_OK)
