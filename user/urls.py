from django.urls import path

from user.views import UserView


urlpatterns = [
    path('user', UserView().as_view()),
]