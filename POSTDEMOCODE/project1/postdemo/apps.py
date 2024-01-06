from django.apps import AppConfig


class PostdemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'postdemo'


    def ready(self):
        import postdemo.signals