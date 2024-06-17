# sms/utils.py

import requests
from django.conf import settings

def send_sms(to, message):
    url = settings.TERMII_BASE_URL
    payload = {
        'to': to,
        'from': settings.TERMII_SENDER_ID,
        'sms': message,
        'type': 'plain',
        'channel': 'generic',
        'api_key': settings.TERMII_API_KEY
    }
    try:
        response = requests.post(url, json=payload)
        response_data = response.json()
        
        if response.status_code == 200 and response_data.get('message_id'):
            return response_data
        else:
            error_message = response_data.get('message', 'Failed to send SMS')
            raise Exception(error_message)
    except requests.RequestException as e:
        raise Exception(f'HTTP request error: {e}')
    except ValueError:
        raise Exception(f'Invalid response received from Termii: {response.text}')
