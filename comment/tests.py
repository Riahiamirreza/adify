from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory

from user.models import User
from advertisement.models import Ad
from comment.models import Comment
from comment.views import CommentView


class TestCreateComment(TestCase):
    @classmethod
    def setUp(cls):
        cls.request_factory = APIRequestFactory()
        cls.user_one = User.objects.create_user(username='un-1', password='123', email='a@mail.ok')
        cls.user_two = User.objects.create_user(username='un-2', password='456', email='b@mail.ok')
        cls.ad_one = Ad.objects.create(id=1, title='t-1', content='c-1', author=cls.user_one)
        cls.ad_two = Ad.objects.create(id=2, title='t-2', content='c-2', author=cls.user_two)

    def test_create_comment(self):
        comment_data = {'ad_id': 1, 'content': 'ok'}
        request = self.request_factory.post('/comment', data=comment_data)
        request.user = self.user_one
        request.data = comment_data
        self.assertFalse(self.ad_one.comment_set.exists())
        response = CommentView().post(request=request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(self.ad_one.comment_set.exists())
