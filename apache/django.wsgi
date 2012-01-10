import os

from django.core.handlers.wsgi import WSGIHandler


os.environ['DJANGO_SETTINGS_MODULE'] = 'in_one_ear.settings'
application = WSGIHandler()
