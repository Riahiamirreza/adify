from unittest.mock import patch

from django.test import TestCase
from rest_framework.test import APIRequestFactory

from advertisement.models import Ad
from advertisement.views import AdvertisementView


class TestGetAdvertisement(TestCase):
    @classmethod
    def setUp(cls):
        Ad(id=1, title='title-1', content='content-1').save()
        Ad(id=2, title='title-2', content='content-2').save()

    def test_get_advertisement(self):
        factory = APIRequestFactory()
        request = factory.get('/advertisement/x')

        response = AdvertisementView().get(request=request, ad_id=1)
        self.assertEqual(response.status_code, 200)

        response = AdvertisementView().get(request=request, ad_id=2)
        self.assertEqual(response.status_code, 200)

    def test_get_nonexistent_advertisement(self):
        factory = APIRequestFactory()
        request = factory.get('/advertisement/x')

        response = AdvertisementView().get(request=request, ad_id=123)  # does not exist
        self.assertEqual(response.status_code, 404)

class TestDeleteAdvertisement(TestCase):
    @classmethod
    def setUp(cls):
        Ad(id=1, title='title-1', content='content-1').save()

    def test_delete_advertisement(self):
        factory = APIRequestFactory()
        request = factory.get('/advertisement/x')

        self.assertTrue(Ad.objects.filter(id=1).exists())
        response = AdvertisementView().delete(request=request, ad_id=1)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Ad.objects.filter(id=1).exists())

    def test_delete_nonexistent_advertisement(self):
        factory = APIRequestFactory()
        request = factory.get('/advertisement/x')

        response = AdvertisementView().delete(request=request, ad_id=123)
        self.assertEqual(response.status_code, 404)
