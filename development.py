# -*- coding: utf-8 -*-
from .common import *

#BASIC
DEBUG = False
DEVELOPMENT = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
ALLOWED_HOSTS = ['app.outset.vc', 'dev.outset.vc']
SECRET_KEY = ''


# EXTENSIONS
INSTALLED_APPS += (
    'djangosecure',
    'gunicorn',
    'storages',
)

SECURITY_MIDDLEWARE = ['djangosecure.middleware.SecurityMiddleware']

# Make sure djangosecure.middleware.SecurityMiddleware is listed first
MIDDLEWARE = SECURITY_MIDDLEWARE + MIDDLEWARE

# SITE CONFIGURATION
# set this to 60 seconds and then to 518400 when you can prove it works
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)
SECURE_FRAME_DENY = env.bool("DJANGO_SECURE_FRAME_DENY", default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool("DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True)
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True

# EMAIL
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Outset <info@outset.vc>'


# CACHING
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# SOCIAL AUTH CONFIG
SOCIAL_AUTH_ANGEL_KEY = ''
SOCIAL_AUTH_ANGEL_SECRET = ''
SOCIAL_AUTH_ANGEL_TOKEN = ''

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = ''
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = ''
