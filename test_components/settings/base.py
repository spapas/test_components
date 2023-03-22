"""
Django settings for test_components project.
"""

import os
from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = "7x=ion&zd9%_hqv0)zc^rh6e#p$jw(8m#xqvt_viqb#fqv(n@+"
DEBUG = False
SITE_ID = 3

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "test_components.core",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "compressor",
    "crispy_forms",
    "crispy_bootstrap5",
    "django_extensions",

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "reversion.middleware.RevisionMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_tools.middlewares.ThreadLocal.ThreadLocalMiddleware",
]

ROOT_URLCONF = "test_components.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "builtins": [
                "django_components.templatetags.component_tags",
            ],
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    [
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                    ],
                )
            ],
        },
    }
]

WSGI_APPLICATION = "test_components.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


LOGIN_REDIRECT_URL = reverse_lazy("home")
LOGIN_URL = "/login/"
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

LANGUAGE_CODE = "el"
TIME_ZONE = "Europe/Athens"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = "/home/serafeim/test_components/static"
STATIC_URL = "/static_test_components/"
MEDIA_URL = "/media_test_components/"
MEDIA_ROOT = "/home/serafeim/test_components/media"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
