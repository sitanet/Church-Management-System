from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)

class FollowAppConfig(AppConfig):
    name = 'follow_app'

    def ready(self):
        logger.info("Starting the scheduler...")
        from . import scheduler
        scheduler.start()
