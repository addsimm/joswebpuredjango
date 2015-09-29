import os,sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# Google App Engine imports.
from google.appengine.ext.webapp import util

# Force Django to reload its settings.
from django.conf import settings
settings._target = None

import django.core.handlers.wsgi

# !!! AS: changed to "app" with GAE
app = django.core.handlers.wsgi.WSGIHandler()