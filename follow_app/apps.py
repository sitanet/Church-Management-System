from django.apps import AppConfig

class FollowAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'follow_app'

    def ready(self):
        print("Starting scheduler...")
        from .tasks import start_scheduler
        start_scheduler()
