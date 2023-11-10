

import os
from decouple import config

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f"welearn.settings.{config('SETTINGS')}")

application = get_wsgi_application()
