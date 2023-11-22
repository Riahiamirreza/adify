from rest_framework import serializers

from advertisement.models import Ad

from comment.serializers import CommentSerializer
from user.serializers import UserSerializer


class AdSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, source='comment_set')
    author = UserSerializer()

    class Meta:
        model = Ad
        fields = '__all__'
