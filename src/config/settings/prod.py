from config.settings.base import *  # NOQA

SECRET_KEY = "django-insecure-7e66^ripfo(8f1b%-(l^xa_+hmx9e8f-!z%8txb)ij-o4ff@r$"


DEBUG = False

ALLOWED_HOSTS = []  # NOQA

INSTALLED_APPS += []  # NOQA

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}


STATIC_URL = "static/"
