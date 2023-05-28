from .base import *

DEBUG = False

SECRET_KEY = config("SECRET_KEY", "b6ns^&+%1+^gq6yuoubmc$z0e&nln-q3w)d4h57$iimvi3z2jc")
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
