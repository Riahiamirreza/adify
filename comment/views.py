from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from advertisement.models import Ad
from comment.models import Comment
from comment.serializers import CommentSerializer


class CommentView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        ad_id = request.data.get('ad_id')
        content = request.data.get('content')
        ad = Ad.objects.filter(id=ad_id).get()
        comment = Comment()
        comment.ad = ad
        comment.content = content
        comment.author = request.user
        comment.save()
        return Response(data={'id': comment.id}, status=201)
