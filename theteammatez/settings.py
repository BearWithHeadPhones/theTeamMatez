"""
Django settings for theteammatez project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q)rp+@r2o&fsgs+4ys1@gf86a!aci9#q3)rn0g%ddy-zrlkilr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'teamMatez','teamz','votez','statistics','django-storages', 'boto',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'theteammatez.urls'

WSGI_APPLICATION = 'theteammatez.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates').replace('\\','/')

)


LOGIN_URL='/login/'
LOGIN_REDIRECT_URL ='/'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

AWS_STORAGE_BUCKET_NAME = "theteammatez"
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
MEDIA_URL = "https://%s.s3.amazonaws.com/" % os.environ['AWS_STORAGE_BUCKET_NAME']
MEDIA_ROOT = ''
AWS_ACCESS_KEY_ID = "AKIAJ7MU7YYH3YXRXJQA"
AWS_SECRET_ACCESS_KEY = "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"

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

DEBUG = False

try:
    from .local_settings import *
except ImportError:
    pass
