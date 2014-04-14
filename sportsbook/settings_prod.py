"""
Django settings for sportsbook project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from settings_general import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mystatbook',
        'USER': 'mystatbook',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/opt/static/mystatbook'

MEDIA_URL='/media/'

MEDIA_ROOT = '/opt/media/mystatbook'

