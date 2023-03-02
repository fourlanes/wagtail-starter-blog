from .base import *

DEBUG = False

# For Admin Emails
ADMINS = [
    ("Edwin", "emagezi@gmail.com"),
]

try:
    from .local import *
except ImportError:
    pass
