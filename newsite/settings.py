"""
Django settings for newsite project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import asynchat
from pathlib import Path
from os import getenv
from .jazzmin import JAZZMIN_SETTINGS

from .email_settings import GMAIL_EMAIL, GMAIL_PASSWORD
from .email_settings import EMAIL_BACKEND, EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_USE_TLS, EMAIL_USE_SLL
from getpass import getpass

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--+o!0!fo3(mu1-zj)vvlmh#s_9$um)zxb%w&nqtmjyn!z2gl9w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("IS_DEVELOPEMENT", True)
#                                 BUG: False, creates staticfiles problems!


ALLOWED_HOSTS = [
    getenv("MY_APP_HOST"),
    'localhost',
    'antenen21.pythonanywhere.com',
]



GMAIL_EMAIL = GMAIL_EMAIL
GMAIL_PASSWORD = GMAIL_PASSWORD



# Imports from email_settings.py
EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = EMAIL_HOST
EMAIL_PORT = EMAIL_PORT
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_USE_SLL = EMAIL_USE_SLL





# Application definition
INSTALLED_APPS = [
    
    'contact',
    'cart', 
    'members',
    'shop',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'newsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
    'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'newsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_ROOT = BASE_DIR / "staticfiles" # for deploy

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]



MEDIA_URL = "/media/"    
# In the models we declare under the ImageField to upload all images 
# from the admin pannel in the "products" folder which comes just like that /media/products.

# In the Data Base the Images aren't stored, only there paths starting like that products/image.png
# So basically when you upload from the Admin Pannel, you store your images in the products folder and the path in the Data Base.
# Images are static files which are visible in the Front-end, Data coming from the Back-end, if this Data would come direct from
# the Data Base, this would be a possible Entry for Hackers.
# So we store only the URL Path in it to protect our Data Base.

MEDIA_ROOT = BASE_DIR / "media"    # Telling Django that this folder with the name "media" we created is the main folder where 
                                   # the medias will be stored and Django needs to look for.  


SITE_ID = 1                         # Added after jassmin instalation creating an new user -> db problems -> now working
JAZZMIN_SETTINGS = JAZZMIN_SETTINGS # we create the jazzmin.py file with the seetings inside to not polluate it here.
                                    # import it with    from .jazzmin import JAZZMIN-SETTINGS
                                    # then tell django that the imported jazzmin-settings are the jazzmin-settings
