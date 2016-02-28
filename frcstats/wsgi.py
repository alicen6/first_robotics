"""
WSGI config for frcstats project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys


# Activate your virtual env
activate_env=os.path.expanduser("venv/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/ec2-user/git/first_robotics/frcstats')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "frcstats.settings")

application = get_wsgi_application()
