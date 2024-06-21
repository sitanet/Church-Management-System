import requests

def send_sms(phone_number, message):
    api_key = 'YOUR_TERMI_API_KEY'  # Replace with your Termii API key
    sender_id = 'YOUR_SENDER_ID'    # Replace with your Termii sender ID
    url = 'https://api.ng.termii.com/api/sms/send'

    payload = {
        'api_key': api_key,
        'to': phone_number,
        'from': sender_id,
        'sms': message,
        'type': 'plain',
        'channel': 'generic',
    }

    response = requests.post(url, json=payload)
    response_data = response.json()

    if response.status_code == 200 and response_data.get('status') == 'ok':
        return f'Successfully sent SMS to {phone_number}'
    else:
        raise Exception(f'Failed to send SMS: {response_data.get("message", "Unknown error")}')

