# -*- coding: utf-8 -*-
"""
Django settings for outset project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from __future__ import absolute_import, unicode_literals
import environ

ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
APPS_DIR = ROOT_DIR.path('outset')

env = environ.Env()

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin
    'django.contrib.admin',
)
THIRD_PARTY_APPS = (
    'tagging',
    'rest_framework',
    'rest_framework_swagger',
    'django_crontab',
    'compressor',
    'django_ses',
    'dbbackup',
    'oauth2_provider',
    'django_filters',
    'corsheaders',
    'safedelete',
    # 'oauth2client.contrib.django_util',
    'social_django',
    'django_object_actions'
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'outset.accounts',  # custom users app
    'outset.accounts.jsontoken',
    'outset.accelerators',
    'outset.finicity',
    'outset.startups',
    'outset.todos',
    'outset.invitations',
    'outset.kpis',
    'outset.activities',
    'outset.backups',
    'outset.billing',
    'outset.updates',
    'outset.yarn',
    'outset.rest_cache',
    'outset.notes_and_docs',
    'outset.doc',
    'outset.oauth2provider',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
]

# MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
MIGRATION_MODULES = {
    'sites': 'outset.contrib.sites.migrations'
}

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)
DEVELOPMENT = False

# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ("""Alex Vykaliuk""", 'alex.vykaliuk@toptal.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'outset_local',
        'USER': 'outset',
        'PASSWORD': '8EkT8b9e',
        'HOST': 'localhost',
        'PORT': '',
    }
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'
DATE_FORMAT = '%Y-%m-%d'
DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

USE_SSL = False

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'outset.processors.settings_response'
            ],
        },
    },
]

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('static'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    # Static folder with generated frontend content
    str(APPS_DIR.path('static')),
    # Static folder with common not modified elements
    str(APPS_DIR.path('prime_static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
)

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# SOCIAL AUTH SETTINGS
REST_SOCIAL_OAUTH_REDIRECT_URI = '/loginSocial'
SOCIAL_AUTH_USER_FIELDS = ['email', 'first_name', 'last_name']

# Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '892308907618-st5nqnv00h9t8qm1hm9vu5o6v1q29lc1.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Nc-LtcbLthRksNcry5xNsrxy'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email']

# ANGEL_API_URL = 'https://api.angel.co/1/'
# SOCIAL_AUTH_ANGEL_AUTH_EXTRA_ARGUMENTS = {'scope': 'email'}

# LinkedIn
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '77ya8w75m0ew32'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'FpUkHH51xHXYol5T'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_basicprofile', 'r_emailaddress']
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = [
    'picture-url',
    'first-name',
    'public-profile-url',
    'last-name',
    'email-address',
    'headline',
    'industry',
    'picture-url',
]


# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'social.backends.linkedin.LinkedinOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


SOCIAL_AUTH_PIPELINE = [
    'outset.accounts.pipelines.auto_logout',

    # Get the information we can about the user and return it in a simple
    # format to create the user instance later. On some cases the details are
    # already part of the auth response from the provider, but sometimes this
    # could hit a provider API.
    'social_core.pipeline.social_auth.social_details',

    # Get the social uid from whichever service we're authing thru. The uid is
    # the unique identifier of the given user in the provider.
    'social_core.pipeline.social_auth.social_uid',

    # Verifies that the current auth process is valid within the current
    # project, this is were emails and domains whitelists are applied (if
    # defined).
    'social_core.pipeline.social_auth.auth_allowed',

    'outset.accounts.pipelines.check_for_email',

    # 'outset.accounts.pipelines.create_accelerator',
    # 'block sign up via google'

    # Checks if the current social-account is already associated in the site.
    'social_core.pipeline.social_auth.social_user',

    # 'outset.accounts.pipelines.process_invite',

    # 'outset.accounts.pipelines.require_email',

    # Make up a username for this person, appends a random string at the end if
    # there's any collision.
    # 'social.pipeline.user.get_username',

    # Send a validation email to the user to verify its email address.
    # Disabled by default.
    # 'social.pipeline.mail.mail_validation',

    # Associates the current social details with another user account with
    # a similar email address. Disabled by default.
    'social_core.pipeline.social_auth.associate_by_email',

    'outset.accounts.pipelines.check_invite',

    'outset.accounts.pipelines.check_safedelete',

    # Create a user account if we haven't found one yet.
    'social_core.pipeline.user.create_user',

    # 'outset.accounts.pipelines.unpack_lazy_user',

    # Create the record that associated the social account with this user.
    'social_core.pipeline.social_auth.associate_user',

    # Populate the extra_data field in the social record with the values
    # specified by settings (and the default ones like access_token, etc).
    'social_core.pipeline.social_auth.load_extra_data',

    # Update the user record with any changed info from the auth service.
    'social_core.pipeline.user.user_details',

    'outset.accounts.pipelines.save_avatar',
    'outset.accounts.pipelines.save_social_connections',

    'outset.accounts.pipelines.extra_user_fields',

    # 'outset.accounts.pipelines.save_avatar',
]

FIELDS_STORED_IN_SESSION = ['invite']
USER_FIELDS = ['email', ]


# Custom user app defaults
# Select the correct user model
AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = '/api_docs/'

# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'

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
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
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
            'handlers': ['console', 'mail_admins'],
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
        },
    }
}

# Cronjob declarations
CRONJOBS = [
    ('14 0 * * *', 'outset.kpis.cron.collect_data'),
    ('0 0 * * *', 'outset.backups.cron.backup'),
    ('0 0 * * *', 'outset.todos.cron.update_everyday_activities'),
    ('0 7 * * *', 'outset.todos.cron.send_reminder_emails'),
    ('1 0 * * 1', 'outset.updates.cron.send_weekly_update_notifications'),
    ('10 0 1 * *', 'outset.updates.cron.send_monthly_update_notifications'),
    ('20 0 1 1,4,7,10 *', 'outset.updates.cron.send_quarterly_update_notifications'),
    ('15 2 * * *', 'outset.cron.remove_non_active_objects'),
    ('2 5 1 * *', 'outset.finicity.cron.sync_institution_list'),
    ('30 2 * * *', 'outset.startups.cron.remove_old_temp_finicity'),
    ('0 0 * * *', 'outset.notes_and_docs.cron.update_google_watch_channel_expires'),
]

LOGIN_URL = 'login'
LOGIN_ERROR_URL = LOGIN_URL

PROJECT_VERSION = 'v1'

OAUTH2_PROVIDER = {
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope',
    }
}
REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False,
    'DATE_INPUT_FORMATS': [DATE_TIME_FORMAT, DATE_FORMAT],
    'DEFAULT_PERMISSION_CLASSES': (
        'outset.billing.permissions.APIAccessPermission',
        'outset.permissions.TokenHasReadWriteScope',
        'outset.permissions.OAuthReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        'outset.accounts.jsontoken.authentication.JsonTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

#DBBACKUP
DBBACKUP_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DBBACKUP_STORAGE_OPTIONS = {
    'access_key': 'AKIAIXNVRDSSXJDQ5ZBQ',
    'secret_key': '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',
    'bucket_name': 'outset-backups'
}

# For celery and others
REDIS_SERVER = 'redis://localhost:6379/0'

FONT_PATH = ROOT_DIR.path('fonts')

if DEBUG:
    SOCIAL_AUTH_PIPELINE = (
        SOCIAL_AUTH_PIPELINE[:2] + 'social.pipeline.debug.debug' +
        SOCIAL_AUTH_PIPELINE[2:])

# django-cors-headers
CORS_ALLOW_HEADERS = (
    'authorization',
    'content-type',
    'origin',
)

# django-tagging
FORCE_LOWERCASE_TAGS = True

# API KEYS
PRIVATE_STRIPE_API_KEY = 'pk_test_ptVPljhiZ5o2riTQpCQqrWKY'
PUBLIC_STRIPE_API_KEY = 'sk_test_RvfUBq4l6cANH1JWcUEU6Xxx'

STRIPE_CLIENT_ID = 'ca_9xcdfmRQXWYGJqARpKtUvpzpKfBJYO56'
STRIPE_REDIRECT_URL = '/accessStripe'
STRIPE_SCOPE = 'read_only'
XERO_CUSTOMER_KEY = 'ZHYWNEAV82BVEP1JHSPLKV4P5J5X84'
XERO_CUSTOMER_SECRET = 'SQ8BSFD1AFMLV0BKHGPOZ1OK4QFGJH'
XERO_REDIRECT_TO = '/accessXero/{}'
XERO_USER_AGENT = 'Outset'
FINICITY_PARTNER_ID = '2445581806937'
FINICITY_PARTNER_SECRET = '6zeltIhce76JXSaLws7P'
FINICITY_APP_KEY = '208bb4232945f327eaacafdb7c390565'


# rest_cache
REST_DEFAULT_CACHE_BY_METHOD = True
REST_DEFAULT_CACHE_BY_PATH = True


# notes_and_docs
NAD_S3_ACCESS_KEY = 'AKIAJUKD5S56WXAOEPFA'
NAD_S3_SECRET_KEY = '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'
NAD_S3_BUCKET_NAME = 'outset-docs-master'
# oauth2client.contrib.django_util
GOOGLE_OAUTH2_CLIENT_ID = SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
GOOGLE_OAUTH2_CLIENT_SECRET = SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
GOOGLE_OAUTH2_SCOPES = ('email', 'https://www.googleapis.com/auth/drive')
GOOGLE_OAUTH2_REDIRECT_TO = '/accessGoogle'
