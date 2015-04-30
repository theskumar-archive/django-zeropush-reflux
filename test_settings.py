DEBUG = True
USE_TZ = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}
ROOT_URLCONF = "zeropush.urls"
INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "zeropush",
)
SITE_ID = 1
MIDDLEWARE_CLASSES = ()
SECRET_KEY = "thisissupersecretkeyfortestingpurpose"
