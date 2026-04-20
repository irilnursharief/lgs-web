# config/settings.py
from pathlib import Path
from dotenv import load_dotenv
import os
import sys

# Load .env file
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(BASE_DIR / "apps"))

# =============================================================================
# CORE
# =============================================================================
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG", "False") == "True"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

# =============================================================================
# APPLICATIONS
# =============================================================================
INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "core",
]

if DEBUG:
    INSTALLED_APPS += ["django_browser_reload"]

# =============================================================================
# MIDDLEWARE
# =============================================================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    MIDDLEWARE += ["django_browser_reload.middleware.BrowserReloadMiddleware"]

# =============================================================================
# URLS & WSGI
# =============================================================================
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# =============================================================================
# TEMPLATES
# =============================================================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "core.context_processors.nav_links",
                "core.context_processors.methodology_steps",
                "core.context_processors.testimonials",
                "core.context_processors.clients",
                "core.context_processors.footer_links",
            ],
        },
    },
]

# =============================================================================
# DATABASE
# =============================================================================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# =============================================================================
# STATIC FILES
# =============================================================================
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

if not DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# =============================================================================
# SECURITY (production)
# =============================================================================
if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = "DENY"

# =============================================================================
# INTERNATIONALISATION
# =============================================================================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Manila"
USE_I18N = True
USE_TZ = True

# =============================================================================
# DEFAULT PRIMARY KEY
# =============================================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =============================================================================
# EMAIL
# =============================================================================
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")
CONTACT_RECIPIENTS = os.environ.get("CONTACT_RECIPIENTS", "").split(",")
