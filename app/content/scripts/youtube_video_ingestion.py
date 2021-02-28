import os
import signal
import sys

ROOT_FOLDER = os.path.realpath(os.path.dirname(__file__))
ROOT_FOLDER = ROOT_FOLDER[:ROOT_FOLDER.rindex('/progress_calculation')]
ROOT_FOLDER = ROOT_FOLDER[:ROOT_FOLDER.rindex('/')]

os.environ['DJANGO_SETTINGS_MODULE'] = 'apps.settings'

if ROOT_FOLDER not in sys.path:
    sys.path.insert(1, ROOT_FOLDER + "/")
import django

django.setup()

