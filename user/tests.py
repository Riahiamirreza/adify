from rest_framework import status
from rest_framework.test import APIRequestFactory

from django.test import TestCase

from user.models import User
from user.views import UserView


class TestCreateUser(TestCase):
    @classmethod
    def setUp(cls):
        cls.request_factory = APIRequestFactory()
        cls.test_user_one = User.objects.create_user(username='un-1', password='123', email='un1@mail.ok')

    def test_create_user(self):
        user_data = {'username': 'Ali', 'password': 'StrongPass', 'email': 'ali@mail.ok'}
        request = self.request_factory.post('/user', data=user_data)
        request.data = user_data
        self.assertFalse(User.objects.filter(username='Ali').exists())
        response = UserView().post(request=request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='Ali').exists())

    def test_create_duplicate_user(self):
        user_data = {'username': 'un-1', 'password': 'StrongPass', 'email': 'un1@mail.ok'}
        request = self.request_factory.post('/user', data=user_data)
        request.data = user_data
        response = UserView().post(request=request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        user_data = {'username': 'un-1', 'password': 'StrongPass', 'email': 'new@mail.ok'}
        request = self.request_factory.post('/user', data=user_data)
        request.data = user_data
        response = UserView().post(request=request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        user_data = {'username': 'new', 'password': 'StrongPass', 'email': 'un1@mail.ok'}
        request = self.request_factory.post('/user', data=user_data)
        request.data = user_data
        response = UserView().post(request=request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_by_invalid_parameters(self):
        user_data = {'username': 'Reza', 'password': 'StrongPass'}
        request = self.request_factory.post('/user', data=user_data)
        request.data = user_data
        response = UserView().post(request=request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        user_data = {'username': 'Mammad', 'email': 'mammad@mail.ok'}
        request = self.request_factory.post('/user', data=user_data)
        request.data = user_data
        response = UserView().post(request=request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        user_data = {'email': 'mammad@mail.ok', 'password': '123'}
        request = self.request_factory.post('/user', data=user_data)
        request.data = user_data
        response = UserView().post(request=request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
