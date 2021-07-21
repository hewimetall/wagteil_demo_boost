"""
WSGI config for wagtail_bootstrap_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wagtail_bootstrap_blog.settings.dev")


from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('x', 'x')

application = get_wsgi_application()
