# myapp/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string

@shared_task
def send_birthday_wish_email(email, first_name):
    subject = 'Happy Birthday!'
    message = render_to_string('admin_staff/birthday_wish.html', {'customer_name': first_name})
    from_email = 'sitanetglobaltech@gmail.com'  # Update with your email
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
