"""
Django settings for PIEDU project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ky13zdk^(*z8r0hmybft9q=(#!_h$pbhbf!77ecg9l==ikjbvg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #
    'mptt',
    'haystack',
    'widget_tweaks',

    #
    'rest_framework',

    #
    'machina',
    'machina.apps.forum',
    'machina.apps.forum_conversation',
    'machina.apps.forum_conversation.forum_attachments',
    'machina.apps.forum_conversation.forum_polls',
    'machina.apps.forum_feeds',
    'machina.apps.forum_moderation',
    'machina.apps.forum_search',
    'machina.apps.forum_tracking',
    'machina.apps.forum_member',
    'machina.apps.forum_permission',

    #
    'debug_toolbar',
    # 'guardian',
    'reportlab',
    'core',
    'api',
    'course',
    'syllabus',
    'PIEDU'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # debug_toolbar_MIDDDLEWARE
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'PIEDU.middleware.HttpPostTunnelingMiddleware'

    # Machina
    'machina.apps.forum_permission.middleware.ForumPermissionMiddleware',

    #Whitenoise
    # 'whitenoise.middleware.WhiteNoiseMiddleware',

]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    # 'guardian.backends.ObjectPermissionBackend',
)

ROOT_URLCONF = 'PIEDU.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "../client/templates"),
            os.path.join(BASE_DIR, "../client/templates/forum")
        ],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Machina
                'machina.core.context_processors.metadata',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]

WSGI_APPLICATION = 'PIEDU.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lmsv3'   ,
        'USER': 'root',
        'PASSWORD': '1234',
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/client/static/'

# debug_toolbar_IPS
INTERNAL_IPS = ['127.0.0.1']


#Extened User Model
AUTH_USER_MODEL = 'core.User'

from machina import MACHINA_MAIN_STATIC_DIR

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../client/static'),
    MACHINA_MAIN_STATIC_DIR,
)

STATIC_ROOT = os.path.join(BASE_DIR, '../client/staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, '../server/uploads')

MEDIA_URL = '/server/uploads/'

LOGOUT_REDIRECT_URL = 'homepage'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'machina_attachments': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp',
    },
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# SECRET_KEY = config('SECRET_KEY')
# DEBUG = config('DEBUG', default=False, cast=bool)

# mysql://b1d9b9e2c747e3:1e808974@us-cdbr-iron-east-01.cleardb.net/heroku_d8c1c07035d581a?reconnect=true
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         # 'NAME': 'heroku_d8c1c07035d581a',
#         # 'USER': 'b1d9b9e2c747e3',
#         # 'PASSWORD': '1e808974',
#         # 'HOST': 'us-cdbr-iron-east-01.cleardb.net',
#         # 'PORT': '',
#         ##
#         'NAME': 'sql12264035',
#         'USER': 'sql12264035',
#         'PASSWORD': 'dgv4jMDekg',
#         'HOST': 'sql12.freemysqlhosting.net',
#         'PORT': '3306',
#
#     }
# }