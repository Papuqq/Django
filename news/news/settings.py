"""
Django settings for news project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0@7v7&85jlx!1-7r)o9@b*-)&)lqejiz48lkt!ps*0_vx+p!+c'

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
    'django.contrib.sites',
    'django.contrib.flatpages',
    'project',
    'django_filters',
    "django_apscheduler",

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',

]

ROOT_URLCONF = 'news.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path .join(BASE_DIR, 'project/templates/project')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'news.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_REDIRECT_URL = "/post"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "example@yandex.ru"
EMAIL_HOST_PASSWORD = "iliezvcovrxqizez"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "example@yandex.ru"

SERVER_EMAIL = "example@yandex.ru"
MANAGERS = (
    ('Ivan', 'ivan@yandex.ru'),
    ('Petr', 'petr@yandex.ru'),
)

ADMINS = (
    ('anton', 'anton@yandex.ru'),
)

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'TIMEOUT': 60, # добавляем стандартное время ожидания в минуту (по умолчанию это 5 минут — 300 секунд)
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'formatters': {
        'debug_console': {
            'format': '%(levelname)s %(message)s %(asctime)s',
            'style': "{"
        },
        'warning_console': {
            'format': '%(levelname)s %(message)s %(asctime)s %(pathname)s',
            'style': "{"
        },
        'errors_console': {
           'format': '%(levelname)s %(message)s %(asctime)s %(pathname)s %(exc_info)s',
           'style': "{"

        },
        'info_file': {
            'format': '%(levelname)s %(message)s %(asctime)s %(module)s',
            'style': "{"
        },
        'security_file': {
            'format': '%(levelname)s %(message)s %(asctime)s %(pathname)s',
            'style': "{"
        },
    },

    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },





    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'debug_console',
        },
        'console_warning': {
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_false'],
            'formatter': 'warning_console'
        },
        'console_error': {
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_false'],
            'formatter': 'errors_console'
        },
        'file_info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'info_file',
            'filters': ['require_debug_false'],
            'filename': 'general.log',
        },
        'errors.log': {
            'level': 'ERROR' 'CRITICAL',
            'class': 'logging.FileHandler',
            'formatter': 'errors_console',
            'filename': 'errors.log',
        },
        'security.log': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'formatter': 'info_file',
            'filename': 'security.log',

        },

    },

    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'console_debug': {
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_false'],
            'formatter': 'debug_console'
        },
        'console_warning': {
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_false'],
            'formatter': 'warning_console'
        },
        'console_error': {
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_false'],
            'formatter': 'errors_console'
        },
        'file_info': {
            'class': 'logging.FileHandler',
            'filters': ['require_debug_true'],
            'formatter': 'info_file',
            'filename': 'general.log'
        },
        'file_errors': {
            'class': 'logging.FileHandler',
            'formatter': 'errors_console',
            'filename': 'errors.log'
        },
        'file_security': {
            'class': 'logging.FileHandler',
            'formatter': 'info_file',
            'filename': 'security.log'
        },
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_true'],
            'formatter': 'security_file',
        }
    },

    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True
        },
        'console': {
            'handlers': ['console_debug'],
            'level': 'DEBUG',
            'propagate': True
        },
        'console_warning': {
            'handlers': ['console_warning'],
            'level': 'WARNING',
            'propagate': True
        },
        'console_error': {
            'handlers': ['console_error'],
            'level': 'ERROR',
            'propagate': True
        },
        'file_info': {
            'handlers': ['file_info'],
            'level': 'INFO',
            'propagate': True
        },
        'django.request': {
            'handlers': ['file_errors', 'mail_admins'],
            'level': 'ERROR' 'CRITICAL',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['file_errors', 'mail_admins'],
            'level': 'ERROR' 'CRITICAL',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['file_errors'],
            'level': 'ERROR' 'CRITICAL',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['file_errors'],
            'level': 'ERROR' 'CRITICAL',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['file_security'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}
