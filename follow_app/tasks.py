import requests
import logging
from .models import Member
from datetime import date
from django.conf import settings

logger = logging.getLogger(__name__)

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
        logger.info(f'SMS sent successfully to {phone_number}')
    else:
        error_message = response_data.get('message', 'Failed to send SMS')
        logger.error(f'Error sending SMS to {phone_number}: {error_message}')

def send_anniversary_sms():
    today = date.today()
    logger.info(f"Checking for anniversaries on {today}")

    # Check for wedding anniversaries
    anniversary_members = Member.objects.filter(
        wedding_ann__isnull=False,
        wedding_ann__month=today.month,
        wedding_ann__day=today.day
    )
    logger.info(f"Found {anniversary_members.count()} members with anniversaries today")

    for member in anniversary_members:
        sms_body = f"Happy Wedding Anniversary {member.first_name}! Wishing you a joyous day!"
        send_sms_via_termii(member.phone_no, sms_body)
