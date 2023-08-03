# testing.py

from .settings import *

# Override settings from settings.py for development environment

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# # SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'caf696b6-ad84-4fe1-ac68-afb779809acd'

# Database settings for testing
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'medic_admin_test',
        'USER': 'medic_admin_test',
        'PASSWORD': 'T3$T_R0N@!_F',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Allowed hosts for development
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Email settings for development (using console backend for debugging)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
