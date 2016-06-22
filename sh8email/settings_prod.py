"""
Django settings for sh8email project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/

#####################################################

If you want to sh8email application with this production settings,
set OS environment variable "DJANGO_SETTINGS_MODULE" to 'sh8email.settings_prod',
using below command.
$ export DJANGO_SETTINGS_MODULE=sh8email.settings_prod
    - by Wonyoung Ju
"""

import os

from .settings_common import BASE_DIR as COMMON_BASE_DIR
from .settings_common import ALLOWED_HOSTS as COMMON_ALLOWED_HOSTS
from .settings_common import INSTALLED_APPS as COMMON_INSTALLED_APPS
from .settings_common import MIDDLEWARE_CLASSES as COMMON_MIDDLEWARE_CLASSES
from .settings_common import ROOT_URLCONF as COMMON_ROOT_URLCONF
from .settings_common import TEMPLATES as COMMON_TEMPLATES
from .settings_common import WSGI_APPLICATION as COMMON_WSGI_APPLICATION
from .settings_common import LANGUAGE_CODE as COMMON_LANGUAGE_CODE
from .settings_common import TIME_ZONE as COMMON_TIME_ZONE
from .settings_common import USE_I18N as COMMON_USE_I18N
from .settings_common import USE_L10N as COMMON_USE_L10N
from .settings_common import USE_TZ as COMMON_USE_TZ
from .settings_common import STATIC_URL as COMMON_STATIC_URL

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = COMMON_BASE_DIR


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SH8EMAIL_DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = COMMON_ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = COMMON_INSTALLED_APPS
MIDDLEWARE_CLASSES = COMMON_MIDDLEWARE_CLASSES
ROOT_URLCONF = COMMON_ROOT_URLCONF

TEMPLATES = COMMON_TEMPLATES

WSGI_APPLICATION = COMMON_WSGI_APPLICATION


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sh8email',
        'USER': 'sh8email',
        'PASSWORD': 'djangoUg0G!rls',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = COMMON_LANGUAGE_CODE

TIME_ZONE = COMMON_TIME_ZONE

USE_I18N = COMMON_USE_I18N

USE_L10N = COMMON_USE_L10N

USE_TZ = COMMON_USE_TZ


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = COMMON_STATIC_URL
