# coding=utf-8

"""
Django settings for EnvMonitor project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from __future__ import unicode_literals

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u(j^h)r)40%&!-%vt(1k!bwrtvlhrp10q!(!gj8o==%g0dynbt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))



TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates').replace('\\', '/'),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'smart_selects',
    'selectable',
    # 'bootstrap3',
    # 'south',
    'company',
    'report',
    'statistics',
    'testapp',

)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'EnvMonitor.urls'

WSGI_APPLICATION = 'EnvMonitor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    # 'default': {
    # 'ENGINE': 'django.db.backends.sqlite3',
    # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'zh-CN'
DEFAULT_CHARSET = 'utf-8'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# add 2014-11-20
# django.contrib.staticfiles 要求设置STATIC_ROOT和MEDIA_ROOT，这样能自动收集所有的静态文件到指定的目录下
STATIC_ROOT = BASE_DIR + '/static/'

MEDIA_ROOT = BASE_DIR + '/media/'


'''This code will try to find a file named local_settings.py in the same directory as the
settings file. If it succeeds, it will import everything defined in the file. If no such file exists,
nothing will happen.'''
try:
    from local_settings import *
except ImportError:
    pass
