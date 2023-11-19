from django.urls import path

from advertisement.views import AdvertiementView


urlpatterns = [
    path('advertisement', AdvertiementView.as_view()),
    path('advertisement/<ad_id>', AdvertiementView.as_view()),
]