from .settings import *

DEBUG = False

# This will be updated with your PythonAnywhere username
ALLOWED_HOSTS = ['Muzammils.pythonanywhere.com']

# Database settings - we'll update these after creating the MySQL database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',  # Will fill this after database creation
        'USER': '',  # Will fill this after database creation
        'PASSWORD': '',  # Will fill this after database creation
        'HOST': '',  # Will fill this after database creation
    }
}

# Static and Media files configuration
STATIC_ROOT = '/home/Muzammils/chat_project/staticfiles'
STATIC_URL = '/static/'

MEDIA_ROOT = '/home/Muzammils/chat_project/media'
MEDIA_URL = '/media/'

# Channel layer configuration for production
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}