from django.urls import path

from advertisement.views import AdvertisementView


urlpatterns = [
    path('advertisement', AdvertisementView.as_view()),
    path('advertisement/<ad_id>', AdvertisementView.as_view()),
]