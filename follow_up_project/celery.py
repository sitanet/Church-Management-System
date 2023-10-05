# # celery.py
# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# from celery.schedules import crontab

# # Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'follow_up_project.settings')

# app = Celery('follow_up_project')

# # Load task modules from all registered Django app configs.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Autodiscover tasks in all installed apps
# app.autodiscover_tasks()


# app.conf.beat_schedule = {
#     'send-periodic-email': {
#         'task': 'follow_app.tasks.send_birthday_emails',  # Replace with the correct path to your task
#         'schedule': crontab(hour=19, minute=0),  # Adjust the time as needed
#     },
# }