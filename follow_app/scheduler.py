import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore, register_events
from .tasks import send_anniversary_sms

logger = logging.getLogger(__name__)

def scheduled_job():
    logger.info("Running scheduled job: send_anniversary_sms")
    send_anniversary_sms()

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # Schedule the job to run daily at 7:50 AM
    scheduler.add_job(
        scheduled_job,
        trigger=CronTrigger(hour="07", minute="50"),
        id="send_anniversary_sms_job",
        replace_existing=True
    )

    register_events(scheduler)
    scheduler.start()
    logger.info("Scheduler started")
