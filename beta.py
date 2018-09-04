# -*- coding: utf-8 -*-
'''
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
'''

from .common import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

USE_SSL = True

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY", default='mf$7%jj!$ugv0bdj(=q9a*=21%i^mrn3=5dpy$%n1axt6%5hls')

ALLOWED_HOSTS = ('app.outset.vc', 'www.app.outset.vc')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'outset',
        'USER': 'outset',
        'PASSWORD': '7zFJ7zZGsPuwqyuGtXdH',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Enable on prod
MIDDLEWARE = [i for i in MIDDLEWARE if i != 'django.middleware.clickjacking.XFrameOptionsMiddleware']

# MEDIA Settings in common STATIC
MEDIA_URL = STATIC_URL + 'media/'
MEDIA_ROOT = STATIC_ROOT + '/media'

# Mail settings
# ------------------------------------------------------------------------------
DEFAULT_FROM_EMAIL = 'hello@outset.vc'
SERVER_EMAIL = 'hello@outset.vc'
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = 'AKIAJUKD5S56WXAOEPFA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_SES_REGION_NAME = 'us-west-2'


# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions', )

# django-cors-headers
# ------------------------------------------------------------------------------
CORS_ORIGIN_ALLOW_ALL = True

# # django-crontab
# # ------------------------------------------------------------------------------
# CRONJOBS = [
#     ('0 0 * * *', 'outset.todos.cron.update_everyday_activities'),
# ]

# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': True
        },
        'django_crontab': {
            'level': 'DEBUG',
            'handlers': ['console', 'mail_admins'],
            'propagate': True
        },
        'outset.notes_and_docs': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': True
        }
    }
}


# django-rest-swagger
# ------------------------------------------------------------------------------
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'description': 'Personal API Key authorization',
            'name': 'Authorization',
            'in': 'header',
        },
        # 'basic_auth': {
        #     'type': 'oauth2',
        #     'authorizationUrl': '/oauth/authorize/',
        #     # 'tokenUrl': '/oauth/authorized_tokens/',
        #     'flow': 'implicit',
        #     'scopes': {
        #     }
        # }
    },
    'USE_SESSION_AUTH': False,
    # 'LOGIN_URL': 'rest_framework:login',
    # 'LOGOUT_URL': 'rest_framework:logout',
    'JSON_EDITOR': False,
}

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Alexander Lupandin', 'alexandr.l@cronix.ms'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

REMOTE_ADDR_REQUEST_HEADER = 'REMOTE_ADDR'
INTERNAL_API_ALLOW_HOSTS = ['localhost', '127.0.0.1', '52.25.47.9', 'app.outset.vc', 'www.app.outset.vc']
INTERNAL_API_ALLOW_ALL = False

# API KEYS
PRIVATE_STRIPE_API_KEY = 'sk_live_jeukqZcLAZF6hVqsQ5HyR8is'
PUBLIC_STRIPE_API_KEY = 'pk_live_b8R0tK8LTNrhTvA6IFtSlobo'
