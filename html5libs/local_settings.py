import logging 

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": "test5",          # Or path to database file if using sqlite3.
        "USER": "postgres",              # Not used with sqlite3.
        "PASSWORD": "",                  # Not used with sqlite3.
        "HOST": "localhost",             # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "5432",                  # Set to empty string for default. Not used with sqlite3.
    }
}

FRAMEWORK_TITLE = "HTML5"
SITE_TITLE = "Modern Web Libraries"

DEBUG = False
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = False
#TEST_RUNNER = 'testrunner.OurTestRunner'

logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s "%(message)s" in %(funcName)s() line %(lineno)d in %(pathname)s', 
        filename='main.log',
        filemode='a',
)

LOCAL_INSTALLED_APPS = []

ROOT_URLCONF = "html5libs.urls"

LAUNCHPAD_ACTIVE = False

# Analytics ID
URCHIN_ID = ""

# Email Settings
DEFAULT_FROM_EMAIL = 'HTML5 Libraries <html5libs@gmail.com>'
EMAIL_SUBJECT_PREFIX = '[HTML5 Libraries] '

# Make this unique, and don't share it with anybody.
SECRET_KEY = "bens_secret_password"

# See http://celeryproject.org/docs/configuration.html#task-execution-settings
CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
BROKER_BACKEND = "django"

LOCAL_INSTALLED_APPS = ('djkombu', )

REGISTRATION_OPEN = True
