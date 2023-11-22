from django.contrib.auth import authenticate, login
from django.db.models import Q

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
            self._validate_user_info(
                username=username,
                password=password,
                email=email
            )
            user = User.objects.create_user(username=username, password=password, email=email)
            return Response(status=status.HTTP_201_CREATED)
        except ValueError as exc:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def _validate_user_info(username: str, password: str, email: str):
        if not (username and password and email):
            raise ValueError(
                "Not valid parameters for user creation"
            )
        if User.objects.filter(Q(email=email) | Q(username=username)).exists():
            raise ValueError(
                "username or email are duplicate"
            )

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if (user := authenticate(request, username=username, password=password)) is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        login(request=request, user=user)
        return Response(status=status.HTTP_200_OK)
