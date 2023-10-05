# # myapp/tasks.py

# from celery import shared_task

# from datetime import datetime
# from .models import Member
# from django.core.mail import send_mail
# from django.template.loader import render_to_string

# @shared_task
# def send_birthday_emails():
#     today = datetime.today().date()
#     customers = Member.objects.filter(date_of_birth__day=today.day,date_of_birth__month=today.month)
#     for customer in customers:
#         subject = 'Happy Birthday!'
#         message = f'Happy birthday, {customer.first_name}!'
#         from_email = 'sitanetglobaltech@gmail.com'
#         recipient_list = [customer.email]
#         send_mail(subject, message, from_email, recipient_list)
