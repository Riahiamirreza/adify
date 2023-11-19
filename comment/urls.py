from django.urls import path

from comment.views import CommentView


urlpatterns = [
    path('comment', CommentView.as_view()),
    path('comment/<comment_id>', CommentView.as_view()),
]