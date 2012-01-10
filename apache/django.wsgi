# Dervied from playdoh.wsgi
import os

from django.core.handlers.wsgi import WSGIHandler

# TODO: Fix up sys.path if necessary. See https://docs.djangoproject.com/en/1.3/howto/deployment/modwsgi/

os.environ['DJANGO_SETTINGS_MODULE'] = 'in_one_ear.settings'
application = WSGIHandler()
