"""
Django settings for laifu project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f7%o*=5rf2i%@g*szvl&mlv+mikn!$n=%%y0gr7jisv%p=kiep'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DatabaseLocal = None
TPLPATH=os.path.join(BASE_DIR, 'static/templates')

ALLOWED_HOSTS = ['*']

# try:
#     from settings_local import *
# except ImportError:
#     pass

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_crontab',
    'users',
    'tasks',
    'management',
    'others',
    'system',
) if DEBUG else (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_crontab',
    # 'debug_toolbar',
    'users',
    'tasks',
    'management',
    'others',
    'system',
) 

MIDDLEWARE_CLASSES = (
    'laifu.middleware.SetRequestDevice',
    'laifu.middleware.WsgiLogErrors',
    # 'laifu.middleware.ExceptionLogging',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'laifu.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TPLPATH,],
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

WSGI_APPLICATION = 'laifu.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shouzhuan',
        'USER': 'shouzhuan123',
        'PASSWORD': 'shouzhuan123$$',
        'HOST': '120.55.64.35',
        'PORT': '3306',
    }

    #     'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'shouzhuan',
    #     'USER': 'root',
    #     'PASSWORD': 'root',
    #     'HOST': '127.0.0.1',
    #     'PORT': '3306',
    # }

    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'xss',
    #     'USER': 'xssroot',
    #     'PASSWORD': 'xss188',
    #     'HOST': 'rds075754z3c8z73180fo.mysql.rds.aliyuncs.com',
    #     'PORT': '3306',
    # }
#   if not DatabaseLocal else DatabaseLocal
}

TEST_RUNNER='laifu.cusrunner.cusrunner'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "../Web/")
# print STATIC_ROOT
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

#session
SESSION_EXPIRE_AT_BROWSER_CLOSE=True

#log
LOG_DIR = os.path.join(BASE_DIR, 'logs/')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'debug': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'debug.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'info':{
            'level':'INFO',
            'class':'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR,'info.log'),
            'when':'MIDNIGHT',
            'backupCount': 7,
            'interval' : 1,
            'formatter':'standard',
        },
        'crontab': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'crontab.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        }
    },
    'loggers': {
        'laifu.crontasks': {
            'handlers': ['console', 'crontab'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True
        },
        'django_crontab.crontab': {
            'handlers': ['console', 'crontab'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True
        },
        'laifu': {
            'handlers': ['console', 'debug', 'info'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True
        },
        'users': {
            'handlers': ['console', 'debug', 'info'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True
        },
        'tasks': {
            'handlers': ['console', 'debug', 'info'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True
        },
        'others': {
            'handlers': ['console', 'debug', 'info'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True
        },
        'management': {
            'handlers': ['console', 'debug', 'info'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True
        },
    }
}

#images
LAIFU_IMAGE_DIR=os.path.join(BASE_DIR, "uploadimage/")

CRONJOBS = [
('0  1 * * *', 'laifu.crontasks.daily_maintenance'),
('*/10 * * * *', 'laifu.crontasks.order_manage'),
]


# DEBUG_TOOLBAR_PATCH_SETTINGS = False
