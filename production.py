# -*- coding: utf-8 -*-
from .common import *

#BASIC
DEBUG = False
DEVELOPMENT = False
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
ALLOWED_HOSTS = ['app.outset.vc', 'dev.outset.vc']
SECRET_KEY = 'xh7akhrq9#11p^voht8e-dadh3qn&v+0^%n5#ap+0o)u$oqhg1'


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
EMAIL_HOST_USER = 'AKIAICGB7OHV2UV3DFWQ'
EMAIL_HOST_PASSWORD = 'Ah6eDceSBsW0LgBc++Od0Qva3Tvh7CJlRAkuYsdQffci'
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
SOCIAL_AUTH_ANGEL_KEY = '9669092cb83dde14d262ab3eef58fbb2d4a6a036d123ed0e'
SOCIAL_AUTH_ANGEL_SECRET = '96939d50442cc0165e7156ffab87f8e9d1a52820a64db33c'
SOCIAL_AUTH_ANGEL_TOKEN = 'f6eef580b30e883d0b0dfa9a396cf6c683ac67024fe109ab'

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '77ya8w75m0ew32'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'FpUkHH51xHXYol5T'
