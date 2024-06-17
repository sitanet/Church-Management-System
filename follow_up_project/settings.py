"""
Django settings for follow_up_project project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import sys
import os
from pathlib import Path
# from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rnrn*r*)!+i0(r&km0$7u+q)6a1-(e))m%4$dbpvm3dov#utj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['followtheminchrist.thecitygatechurch.org']

ALLOWED_HOSTS = []
# Application definition

# INTERNAL_IPS = ['127.0.0']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'follow_app',
    'pastorate',
    # 'celery_results',
    'accounts',
    'coordinators',
    'team_members',
    'facilitator',
    'student',
    'career',
    'business',
    'kbn',
    # 'celery',
    # 'django_celery_beat',
    # 'django_celery_results',
    "django_apscheduler",
    
    
    
]







MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'follow_up_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'follow_up_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('NAME'),
#         'USER': config('USER'),
#         'PASSWORD': config('PASSWORD'),
#         'HOST': config('HOST'),
#         'PORT': 5432,
#     }
# }



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'thecity2_Follow_up',
#         'USER': 'thecity2_follow_up',
#         'PASSWORD': 'People@1234',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'follow_up',
        'USER': 'postgres',
        'PASSWORD': 'People',
        'HOST': 'localhost',
        # 'HOST': 'database-2.cxwm64gcozpx.us-west-2.rds.amazonaws.com',  # Or your database host
        'PORT': '5432',           # Leave empty for the default PostgreSQL port (5432)
    }
}


AUTH_USER_MODEL = 'accounts.User'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = '/home2/thecity2/public_html/followtheminchrist/static/'
# STATIC_ROOT = BASE_DIR /'static'
STATICFILES_DIRS = [
    
    'follow_up_project/static',
    # os.path.join(BASE_DIR, 'your_app/static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home2/thecity2/public_html/followtheminchrist/media/'
# MEDIA_ROOT = BASE_DIR /'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# EMAIL_HOST= config('EMAIL_HOST')
# EMAIL_PORT= config('EMAIL_PORT', cast=int)
# EMAIL_HOST_USER= config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD= config('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'TCGC Followup Team'


EMAIL_HOST= 'smtp.gmail.com'
EMAIL_PORT= 587
EMAIL_HOST_USER='sitanetglobaltech@gmail.com'
# EMAIL_HOST_PASSWORD= 'fgegffwquvukiprs'
EMAIL_HOST_PASSWORD= 'ipudrjbwheuzrxsw'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'TCGC Followup Team'


# Twilio settings
TWILIO_ACCOUNT_SID = 'AC0320290d9bbd6e4de68d2a0032c87e8a'
TWILIO_AUTH_TOKEN = '98af496cc50db558be25032d88bdafee'
TWILIO_PHONE_NUMBER = '+12073864340'



# BULKSMSNIGERIA_API_TOKEN = 'xd70lPWDocemJkKNityTNzSXCEGYtApTbxKs0VrQ0qBWEKv2ABTlcUmNwUJQ'
# BULKSMSNIGERIA_SENDER_ID = '2348066311516'

# Celery settings
# CELERY_BROKER_URL = 'redis://localhost:6379/0'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'


# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/0",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }

# settings.py

# Celery configuration
# CELERY_BROKER_URL = 'redis://localhost:6379/0'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'




# settings.py



# Celery periodic task



# CELERY_BROKER_URL = 'redis://127.0.0.1:6379/1'
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'UTC'


# from celery.schedules import crontab

# CELERY_BEAT_SCHEDULE = {
#     'send-birthday-and-anniversary-sms': {
#         'task': 'follow_app.tasks.send_birthday_and_anniversary_sms',
#         'schedule': crontab(hour=21, minute=0),  # This schedules the task to run daily at midnight
#     },
# }


# APScheduler settings



SCHEDULER_JOBSTORES = {
    'default': {
        'type': 'django_apscheduler.jobstores:DjangoJobStore',
    }
}

SCHEDULER_EXECUTORS = {
    'default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': 20
    }
}

SCHEDULER_JOB_DEFAULTS = {
    'coalesce': False,
    'max_instances': 1
}

# SCHEDULER_TIMEZONE = 'UTC'  # or your preferred timezone

# settings.py

TERMII_API_KEY = 'TLVDYxEuHVSoYXNGzUsQiVIvDADIoWIwULdPmIcSqDrsJblXZcLjzMshonEGBq'
TERMII_BASE_URL = 'https://api.ng.termii.com/api/sms/send'
TERMII_SENDER_ID = 'TCGC MOS'  
