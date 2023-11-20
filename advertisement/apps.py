import os

from django.apps import AppConfig

from dotenv import load_dotenv

class AdvertisementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'advertisement'

    @classmethod
    def _init_(cls, env_path: str = '.env'):
        load_dotenv(env_path)

AdvertisementConfig._init_()
