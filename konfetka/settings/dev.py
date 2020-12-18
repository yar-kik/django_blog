from .settings import *

ALLOWED_HOSTS = ["localhost",
                 "127.0.0.1"]
DEBUG = True

INSTALLED_APPS = [
    'account',
    'articles',
    'images',
    'actions',
    'archives',

    'dal',
    'dal_select2',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'taggit',
    'social_django',
    'sorl.thumbnail',
    'phonenumber_field',
    'debug_toolbar',
    "template_profiler_panel",
    'django.contrib.postgres',
    'ckeditor',
    'ckeditor_uploader',
    'imagekit',
    'environ',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "../static"),
]

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'