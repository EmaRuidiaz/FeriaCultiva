from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'FeriaCultiva',
        'USER': 'ema2019',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
        'DEFAULT_CHARSET': 'utf-8',
    }
}