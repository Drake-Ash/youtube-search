import os
import signal
import sys

ROOT_FOLDER = os.path.realpath(os.path.dirname(__file__))
ROOT_FOLDER = ROOT_FOLDER[:ROOT_FOLDER.rindex('/scripts')]
ROOT_FOLDER = ROOT_FOLDER[:ROOT_FOLDER.rindex('/')]

print(ROOT_FOLDER)

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

if ROOT_FOLDER not in sys.path:
    sys.path.insert(1, ROOT_FOLDER + "/")
import django

django.setup()

from content.services.youtube_service import YoutubeService
from django.utils import timezone
from datetime import timedelta
import time


while True:
    timediff = timezone.now() - timedelta(seconds=60)
    videos_json = YoutubeService.get_videos_from_youtube(timediff)
    YoutubeService.create_or_update_videos(videos_json)
    time.sleep(15)
