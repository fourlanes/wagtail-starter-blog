#!/usr/bin/env python
import os
import sys
from decouple import config

if __name__ == "__main__":
    enviroment = config("ENVIRONMENT", "dev")

    if enviroment.lower() == "production" or enviroment.lower() == "staging":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "consultancy.settings.production")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "consultancy.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
