import dj_database_url

from .base import *
try:
    from .local import *
except ImportError:
    pass


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {"default": dj_database_url.parse(DATABASE_URL, conn_max_age=600)}