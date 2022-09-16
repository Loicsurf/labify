from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ["*"]

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

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_PORT = 587
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'loicsurf20@gmail.com'
# EMAIL_HOST_PASSWORD = 'Ciacia@144'

import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# HTTPS SETTINGS
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

# HSTS SETTINGS
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_PRELOAD = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False