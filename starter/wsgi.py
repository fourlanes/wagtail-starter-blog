"""
WSGI config for starter project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from decouple import config

enviroment = config("ENVIRONMENT", "dev")

if enviroment.lower() == "production" or enviroment.lower() == "staging":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "starter.settings.production")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "starter.settings.dev")

application = get_wsgi_application()
