from django.db import models

from user.models import User


class Ad(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1023)
    author = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)
