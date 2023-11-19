from rest_framework.views import APIView
from rest_framework.response import Response

from user.serializers import UserSerializer


class UserView(APIView):
    serializer_class = UserSerializer
 
    def get_object(self):
        return self.request.user



class LoginView(APIView):
    ...