# follow_app/scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from .tasks import send_birthday_and_anniversary_sms
import logging

logger = logging.getLogger(__name__)

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # Schedule the job using the function reference
    scheduler.add_job(
        send_birthday_and_anniversary_sms,  # Reference to the function
        'cron',
        hour=18,  # 4 PM
        minute=2,
        id='send_birthday_and_anniversary_sms',
        replace_existing=True
    )

    register_events(scheduler)
    scheduler.start()
    logger.info("Scheduler started.")
