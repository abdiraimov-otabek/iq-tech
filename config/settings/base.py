import os
from pathlib import Path
from datetime import timedelta

import dj_database_url
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _

load_dotenv()

# This file lives at config/settings/base.py, so project root is three levels up
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "unsafe-secret")

DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

CSRF_TRUSTED_ORIGINS = os.getenv("CRF_TRUSTED_ORIGINS","").split(",")

# Installed apps
INSTALLED_APPS = [
    "unfold",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party
    "unfold.contrib.forms",
    "rest_framework",
    "rest_framework.authtoken",
    "drf_spectacular",
    "corsheaders",
    "modeltranslation",
    # Local apps
    "apps.team",
    "apps.projects",
    "apps.services",
    "apps.stats",
    "apps.contact",
    "apps.blog",
    "apps.technology",
    "apps.partners",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}

# DATABASES = {
#     "default": {
#         "ENGINE": os.getenv("DB_ENGINE"),
#         "NAME": os.getenv("DB_NAME"),
#         "USER": os.getenv("DB_USER", ""),
#         "PASSWORD": os.getenv("DB_PASSWORD", ""),
#         "HOST": os.getenv("DB_HOST", ""),
#         "PORT": os.getenv("DB_PORT", ""),
#     }
# }


# Authentication
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# Static & Media
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# CORS
CORS_ALLOW_ALL_ORIGINS = True

# Internationalization
LANGUAGE_CODE = "en"
TIME_ZONE = "Asia/Tashkent"
USE_I18N = True
USE_TZ = True

# Swagger
SPECTACULAR_SETTINGS = {
    "TITLE": "IQ Tech Portfolio API",
    "DESCRIPTION": "API backend for IQ Tech portfolio & landing page",
    "VERSION": "1.0.0",
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#leaguages

LANGUAGES = [
    ('en', _('English')),
    ('ru', _('Russian')),
    ('uz', _('Uzbek')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]
MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_LANGUAGES = ('uz', 'ru', 'en')