"""
Django settings for jobber project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ
import dj_database_url
import django_heroku
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
# Load environment variables from .env
env = environ.Env()
if env.bool('DJANGO_READ_DOT_ENV_FILE', default=True):
    env_file = str(os.path.join(BASE_DIR, ".env"))
    if os.path.exists(env_file):
        env.read_env(env_file)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$h7=!ie8*clz36is7b^#+nt!&y&5pj4!2yg+qk1rvuj2_zh-ly'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['127.0.0.1','jobber-vit.herokuapp.com','localhost']


# Application definition

INSTALLED_APPS = [

    #user app
    'users.apps.UsersConfig',
    # jobber_work
    'jobberwork',

    # Oauth
    'dj_rest_auth',
    'allauth',

    # allauth
    'rest_framework.authtoken',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',

    # rest_framework
    'rest_framework',

    # social_oauth
    'allauth.socialaccount.providers.google',
    
    #swagger_docs
    'rest_framework_swagger',

    #other_django_apps    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #site_framework
    'django.contrib.sites',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jobber.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

# custom user model
AUTH_USER_MODEL = 'users.User'

WSGI_APPLICATION = 'jobber.wsgi.application'

# Oauth and Rest framework 

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    
    'UNICODE_JSON': False,
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticatedOrReadOnly',),
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}


SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
    'USE_SESSION_AUTH': False,
    'JSON_EDITOR': True,
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    'DOC_EXPANSION': 'list',
    'APIS_SORTER': 'alpha',
    'SHOW_REQUEST_HEADERS': True,
}


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
DATABASES = {
    "default": {
    'default': {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'jobber',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': 'jobber',
        'PASSWORD': 'jobber123',
        'HOST': 'localhost',
        'PORT': 5432,
        'CONN_MAX_AGE': 60
    }
    }
}


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline',
        },
    },
}


SOCIALACCOUNT_AUTO_SIGNUP = True


REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'dj_rest_auth.serializers.LoginSerializer',
    'TOKEN_SERIALIZER': 'dj_rest_auth.serializers.TokenSerializer',
}



# default_username_field
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static'),]
STATIC_URL = '/static/'
STATIC_ROOT = '/static/'

MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())