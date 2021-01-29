"""
Django dev settings.
"""
from opianalytics.settings.default import *
import os

DEBUG = True
CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ["*"]
WSGI_APPLICATION = 'wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'NAME': settings_secret['DATABASES']['default']['name'],
        'HOST': settings_secret['DATABASES']['default']['host'],
        'USER': settings_secret['DATABASES']['default']['user'],
        'PASSWORD': settings_secret['DATABASES']['default']['password'],
        'PORT': settings_secret['DATABASES']['default']['port']
    }
}
