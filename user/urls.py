from django.urls import path

from user.views import UserView, LoginView


urlpatterns = [
    path('user', UserView().as_view()),
    path('login', LoginView.as_view()),
]