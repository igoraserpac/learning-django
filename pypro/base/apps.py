from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'pypro.base'
    default_auto_field = 'django.db.models.BigAutoField'
