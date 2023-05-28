from .base import *

DEBUG = False

# For Admin Emails
ADMINS = [
    ("Edwin", "emagezi@gmail.com"),
]

ALLOWED_HOSTS = ["line23.co"]
CSRF_TRUSTED_ORIGINS = ["https://suma.ug"]

try:
    from .local import *
except ImportError:
    pass
