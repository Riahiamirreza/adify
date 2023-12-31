from django.db import models

from advertisement.models import Ad
from user.models import User


class Comment(models.Model):
    content = models.TextField(null=False, max_length=1023)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
