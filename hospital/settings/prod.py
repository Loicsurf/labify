from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ["web-production-7c3c.up.railway.app", "labisfy.com", "www.labisfy.com", 'labify.herokuapp.com']

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

EMAIL_BACKEND = config('EMAIL_BACKEND'),
EMAIL_HOST = config('EMAIL_HOST'),
EMAIL_HOST_USER = config('EMAIL_HOST_USER'),
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD'),
EMAIL_PORT = 587
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True

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
