import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from .models import Member
from .utils import send_sms  # Assuming send_sms is in utils.py

def send_birthday_and_anniversary_wishes():
    today = datetime.date.today()

    # Check for birthdays
    members_with_birthday = Member.objects.filter(date_of_birth__month=today.month, date_of_birth__day=today.day)
    for member in members_with_birthday:
        send_birthday_wishes(member)

    # Check for wedding anniversaries
    members_with_anniversary = Member.objects.filter(wedding_ann__month=today.month, wedding_ann__day=today.day)
    for member in members_with_anniversary:
        send_anniversary_wishes(member)

def send_birthday_wishes(member):
    sms_body = f"Happy Birthday, {member.first_name}! Wishing you a blessed year ahead. - The CityGate Church"
    send_sms(member.phone_no, sms_body)

def send_anniversary_wishes(member):
    sms_body = f"Happy Wedding Anniversary, {member.first_name}! Wishing you and your spouse many more blessed years together. - The CityGate Church"
    send_sms(member.phone_no, sms_body)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # Schedule the job to run daily at midnight
    register_job(scheduler, 'cron', hour=0, minute=0, name='send_wishes', jobstore='default')(send_birthday_and_anniversary_wishes)

    register_events(scheduler)
    scheduler.start()
    print("Scheduler started...")
