from django.apps import AppConfig


class FollowAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'follow_app'



# follow_app/apps.py





# follow_app/apps.py

# from django.apps import AppConfig

class FollowAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'follow_app'

    def ready(self):
        from follow_app.scheduler import start
        start()
