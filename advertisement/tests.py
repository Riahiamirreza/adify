from unittest.mock import patch

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory

from advertisement.models import Ad
from advertisement.views import AdvertisementView

from user.models import User


class TestGetAdvertisement(TestCase):
    @classmethod
    def setUp(cls):
        cls.test_user_one = User.objects.create_user(username='un-1', password='123', email='a@a.a')
        cls.test_user_two = User.objects.create_user(username='un-2', password='456', email='b@b.b')
        cls.factory = APIRequestFactory()
        Ad(id=1, title='title-1', content='content-1', author=cls.test_user_one).save()
        Ad(id=2, title='title-2', content='content-2', author=cls.test_user_two).save()

    def test_get_advertisement(self):
        request = self.factory.get('/advertisement/x')

        response = AdvertisementView().get(request=request, ad_id=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['author']['username'], self.test_user_one.username)

        response = AdvertisementView().get(request=request, ad_id=2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['author']['username'], self.test_user_two.username)

    def test_get_nonexistent_advertisement(self):
        request = self.factory.get('/advertisement/x')

        response = AdvertisementView().get(request=request, ad_id=123)  # does not exist
        self.assertEqual(response.status_code, 404)


class TestDeleteAdvertisement(TestCase):
    @classmethod
    def setUp(cls):
        cls.test_user_one = User.objects.create_user(username='un-1', password='123', email='a@a.a')
        cls.test_user_two = User.objects.create_user(username='un-2', password='456', email='b@b.b')
        cls.factory = APIRequestFactory()
        Ad(id=1, title='title-1', content='content-1', author=cls.test_user_one).save()
        Ad(id=2, title='title-2', content='content-2', author=cls.test_user_two).save()

    def test_delete_advertisement(self):
        request = self.factory.get('/advertisement/x')
        request.user = self.test_user_one

        self.assertTrue(Ad.objects.filter(id=1).exists())
        response = AdvertisementView().delete(request=request, ad_id=1)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Ad.objects.filter(id=1).exists())

    def test_delete_nonexistent_advertisement(self):
        request = self.factory.get('/advertisement/x')
        request.user = self.test_user_one

        response = AdvertisementView().delete(request=request, ad_id=123)
        self.assertEqual(response.status_code, 404)

    def test_delete_advertisement_by_unauthorized_user(self):
        request = self.factory.get('/advertisement/x')
        request.user = self.test_user_two

        response = AdvertisementView().delete(request=request, ad_id=1)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        request.user = self.test_user_one
        response = AdvertisementView().delete(request=request, ad_id=2)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
