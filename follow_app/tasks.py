import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import ConflictingIdError
from django_apscheduler.jobstores import DjangoJobStore, register_job
from django.conf import settings
from .models import Member
from .utils import send_sms

def send_birthday_and_anniversary_wishes():
    today = datetime.date.today()
    members_with_birthday = Member.objects.filter(date_of_birth__month=today.month, date_of_birth__day=today.day)
    members_with_anniversary = Member.objects.filter(wedding_ann__month=today.month, wedding_ann__day=today.day)

    for member in members_with_birthday:
        phone_number = member.phone_no
        message = f"Happy Birthday, {member.first_name}! We wish you all the best on your special day. Stay blessed!"
        send_sms(phone_number, message)

    for member in members_with_anniversary:
        phone_number = member.phone_no
        message = f"Happy Wedding Anniversary, {member.first_name}! May your union continue to be blessed and joyful."
        send_sms(phone_number, message)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    job_id = 'send_wishes'
    try:
        scheduler.remove_job(job_id, jobstore='default')
    except Exception as e:
        print(f"No existing job found with ID {job_id}: {e}")

    # Schedule the job to run every minute for testing purposes
    try:
        register_job(scheduler, 'interval', minutes=1, id=job_id, jobstore='default')(send_birthday_and_anniversary_wishes)
        scheduler.start()
    except ConflictingIdError:
        print(f"A job with ID {job_id} already exists.")

    print("Scheduler started!")

