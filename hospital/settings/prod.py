from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ["labisfycom-labisfy.up.railway.app", "labisfy.com", 'labify.herokuapp.com']
CSRF_TRUSTED_ORIGINS = ['https://labisfycom-labisfy.up.railway.app/']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '5555',
    }
}

import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# HTTPS SETTINGS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# HSTS SETTINGS
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
