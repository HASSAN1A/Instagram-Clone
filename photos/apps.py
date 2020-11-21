from django.apps import AppConfig


class PhotosConfig(AppConfig):
    name = 'photos'


    def ready(self):
        import users.signals
