"""
Base settings to build other settings files upon.
"""
import environ
from pathlib import Path

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

###################### {{ cookiecutter.project_slug }}/ ######################
APPS_DIR = ROOT_DIR / "{{ cookiecutter.project_slug }}"
env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR / ".env"))

# GENERAL - https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)
TIME_ZONE = "{{ cookiecutter.timezone }}"
LANGUAGE_CODE = "es-PE"
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [str(ROOT_DIR / "locale")]

# DATABASES - https://docs.djangoproject.com/en/dev/ref/settings/#databases
{% if cookiecutter.use_docker == "y" -%}
DATABASES = {"default": env.db("DATABASE_URL")}
{%- else %}
DATABASES = {
    "default": env.db("DATABASE_URL", default="sqlite:///db.sqlite3")
}
{%- endif %}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# URLS - https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application" # https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application

# APPS
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles", 
    "django.contrib.admin",
    "django.forms",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "allauth",
    "allauth.account",
    # "allauth.socialaccount",
{%- if cookiecutter.use_celery == 'y' %}
    "django_celery_beat",
{%- endif %}
{%- if cookiecutter.use_drf == "y" %}
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    # "dj_rest_auth.registration",
    "corsheaders",
{%- endif %}
]

LOCAL_APPS = [
    "{{ cookiecutter.project_slug }}.users.apps.UsersConfig",
    # Your stuff: custom apps go here
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS # https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps

# MIGRATIONS - https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {"sites": "{{ cookiecutter.project_slug }}.contrib.sites.migrations"}

# AUTHENTICATION - https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

AUTH_USER_MODEL = "users.User"# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
{%- if cookiecutter.use_drf == 'y' %}
# LOGIN_REDIRECT_URL = "users:redirect" # https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
# LOGIN_URL = "account_login" # https://docs.djangoproject.com/en/dev/ref/settings/#login-url
{%- else %}
LOGIN_REDIRECT_URL = "users:redirect" # https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_URL = "account_login" # https://docs.djangoproject.com/en/dev/ref/settings/#login-url
{%- endif %}

# PASSWORDS - https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# MIDDLEWARE - https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
{%- if cookiecutter.use_drf == 'y' %}
    "corsheaders.middleware.CorsMiddleware",
{%- endif %}
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# STATIC - https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
STATIC_URL = "/static/" # https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATICFILES_DIRS = [str(APPS_DIR / "static")] # https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
] # https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders

# MEDIA - https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR / "media")
MEDIA_URL = "/media/" # https://docs.djangoproject.com/en/dev/ref/settings/#media-url

# TEMPLATES - https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        "DIRS": [str(APPS_DIR / "templates")],
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "{{ cookiecutter.project_slug }}.utils.context_processors.settings_context",
            ],
        },
    }
]

# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap4"

# FIXTURES - https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)

# SECURITY - https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True # https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
SECURE_BROWSER_XSS_FILTER = True # https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
X_FRAME_OPTIONS = "DENY" # https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options

# EMAIL - https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env("DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend")
EMAIL_TIMEOUT = 5 # https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
DEFAULT_FROM_EMAIL = "{{cookiecutter.email}}"

# ADMIN
ADMIN_URL = "admin/"

# LOGGING - https://docs.djangoproject.com/en/dev/ref/settings/#logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

{% if cookiecutter.use_celery == 'y' -%}
# CELERY
if USE_TZ:
    
    CELERY_TIMEZONE = TIME_ZONE # http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-timezone
CELERY_BROKER_URL = env("CELERY_BROKER_URL") # http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-broker_url
CELERY_RESULT_BACKEND = CELERY_BROKER_URL # http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_backend
CELERY_ACCEPT_CONTENT = ["json"] # http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-accept_content
CELERY_TASK_SERIALIZER = "json" # http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-task_serializer
CELERY_RESULT_SERIALIZER = "json" # http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_serializer
CELERY_TASK_TIME_LIMIT = 5 * 60 # http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-time-limit
CELERY_TASK_SOFT_TIME_LIMIT = 60 # http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-soft-time-limit
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler" # http://docs.celeryproject.org/en/latest/userguide/configuration.html#beat-scheduler

{%- endif %}
# DJANGO-ALLAUTH - https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
ACCOUNT_AUTHENTICATION_METHOD = "email"  # username | email | username_email
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_ADAPTER = "{{cookiecutter.project_slug}}.users.adapters.AccountAdapter"
SOCIALACCOUNT_ADAPTER = "{{cookiecutter.project_slug}}.users.adapters.SocialAccountAdapter"
# django-allauth | social account providers- https://django-allauth.readthedocs.io/en/latest/providers.html


{% if cookiecutter.use_drf == "y" -%}
# DJANGO-REST-FRAMEWORK - https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        # "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_RENDERER_CLASSES": ("djangorestframework_camel_case.render.CamelCaseJSONRenderer",),
    "DEFAULT_PARSER_CLASSES": (
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
    ),
    "JSON_UNDERSCOREIZE": {
        "no_underscore_before_number": True,
    },
}

# DJ REST AUTH- https://dj-rest-auth.readthedocs.io/en/latest/configuration.html
OLD_PASSWORD_FIELD_ENABLED = True  # If the old password will be askedua
# REST_AUTH_SERIALIZERS = {"USER_DETAILS_SERIALIZER": ".serializers.MyUserSerializer",}
# REST_AUTH_REGISTER_SERIALIZERS = {"REGISTER_SERIALIZER": ".serializers.MyRegisterUserModelSerialzier",}

# SIMPLEJWT - https://github.com/jazzband/django-rest-framework-simplejwt
REST_USE_JWT = False  # If will use jwt
# SIMPLE_JWT = {"AUTH_HEADER_TYPES": ("token",)}# nombre del header Authorization

# DJANGO CORS HEADER - https://github.com/adamchainz/django-cors-headers#setup
CORS_URLS_REGEX = r"^/api/.*$"
# CORS_ALLOW_ALL_ORIGINS = True
{%- endif %}
