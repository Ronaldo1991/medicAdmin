# development.py

from .settings import *

# Override settings from settings.py for development environment

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# # SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '167ca85c-d804-44cf-8910-151ed6dc7ee7'

# Database settings for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'medic_admin_dev',
        'USER': 'medic_admin_dev',
        'PASSWORD': 'D3v_R0N@!_F',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# Allowed hosts for development
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Email settings for development (using console backend for debugging)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
