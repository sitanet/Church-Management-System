import requests
from twilio.rest import Client
from django.conf import settings
from .models import Member
from datetime import date

def send_sms_via_twilio(phone_number, message):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone_number
    )

def send_sms_via_termii(phone_number, message):
    termii_url = 'https://api.ng.termii.com/api/sms/send'
    payload = {
        "to": phone_number,
        "from": settings.TERMII_SENDER_ID,
        "sms": message,
        "type": "plain",
        "channel": "dnd",
        "api_key": settings.TERMII_API_KEY
    }
    response = requests.post(termii_url, json=payload)
    response_data = response.json()
    if response.status_code == 200 and response_data.get('status') == 'success':
        print(f'SMS sent successfully to {phone_number}')
    else:
        error_message = response_data.get('message', 'Failed to send SMS')
        print(f'Error sending SMS to {phone_number}: {error_message}')

def send_birthday_and_anniversary_sms():
    today = date.today()

    # Check for birthdays
    birthday_members = Member.objects.filter(date_of_birth__month=today.month, date_of_birth__day=today.day)
    for member in birthday_members:
        sms_body = f"Happy Birthday {member.first_name}! We wish you a wonderful day!"
        # Replace `send_sms_via_twilio` with `send_sms_via_termii` if you want to use Termii instead
        send_sms_via_termii(member.phone_no, sms_body)

    # Check for wedding anniversaries
    anniversary_members = Member.objects.filter(
        wedding_ann__isnull=False,
        wedding_ann__month=today.month,
        wedding_ann__day=today.day
    )
    for member in anniversary_members:
        sms_body = f"Happy Wedding Anniversary {member.first_name}! Wishing you a joyous day!"
        # Replace `send_sms_via_twilio` with `send_sms_via_termii` if you want to use Termii instead
        send_sms_via_termii(member.phone_no, sms_body)
