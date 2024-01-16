import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-+_(cr#3654v5d_j4!$hx+n0w75b7&7()0l*dsfvhjfdsvhj'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '164.92.254.223']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIR = ['authe', 'fav', 'movies']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')