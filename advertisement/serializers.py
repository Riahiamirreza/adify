from rest_framework import serializers

from advertisement.models import Ad
from comment.serializers import CommentSerializer


class AdSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, source='comment_set')
    class Meta:
        model = Ad
        fields = '__all__'
