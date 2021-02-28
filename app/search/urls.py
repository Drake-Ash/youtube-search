from django.conf.urls import url, include
from rest_framework import routers

from .views import VideoSearchView

video_search = routers.DefaultRouter()
video_search.register("video", VideoSearchView, base_name="video-search")


urlpatterns = [
    url(r'^v1/', include(video_search.urls)),
]
