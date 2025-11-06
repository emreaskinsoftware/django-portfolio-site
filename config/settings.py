from pathlib import Path
from django.urls import reverse_lazy
import os

# ===========================
# TEMEL AYARLAR
# ===========================
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'insecure-dev-key')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

# ===========================
# UYGULAMALAR
# ===========================
INSTALLED_APPS = [
    "pages.apps.PagesConfig",
    "projects.apps.ProjectsConfig",
    "blog.apps.BlogConfig",
    "contact.apps.ContactConfig",
    "ckeditor",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "whitenoise.runserver_nostatic",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# ===========================
# VERİTABANI — SADE (SQLite)
# ===========================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ===========================
# ŞİFRE GÜVENLİĞİ
# ===========================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ===========================
# DİL & ZAMAN
# ===========================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ===========================
# STATİK DOSYALAR
# ===========================
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
if not os.path.exists(BASE_DIR / "static"):
    os.makedirs(BASE_DIR / "static")

# ===========================
# MEDYA DOSYALARI
# ===========================
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ===========================
# CKEDITOR AYARLARI
# ===========================
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "Custom",
        "height": 400,
        "width": "100%",
        "toolbar_Custom": [
            ["Image", "Table"],
            ["CodeSnippet"],
        ],
        "extraPlugins": "codesnippet,image2",
        "filebrowserImageUploadUrl": reverse_lazy("ckeditor_upload"),
        "filebrowserBrowseUrl": reverse_lazy("ckeditor_browse"),
        "image2_uploadUrl": reverse_lazy("ckeditor_upload"),
    }
}

# ===========================
# E-POSTA (GELİŞTİRME)
# ===========================
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
ADMIN_EMAIL = "emreaskinoffical@gmail.com"

# ===========================
# CACHE & RATE LIMIT
# ===========================
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "django-ratelimit-cache",
    }
}
RATELIMIT_RATE = "5/m"
RATELIMIT_BLOCK = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
