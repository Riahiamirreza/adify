from rest_framework.views import APIView
from rest_framework.response import Response

from user.serializers import UserSerializer


class UserView(APIView):
    ...