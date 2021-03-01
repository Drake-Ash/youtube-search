from rest_framework import viewsets

from . import models
from . import serializers


class YoutubeAPIKeyViewSet(viewsets.ModelViewSet):
    queryset = models.YoutubeAPIKey.objects.all()
    serializer_class = serializers.YoutubeAPIKeySerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer


class VideoThumbnailViewSet(viewsets.ModelViewSet):
    queryset = models.VideoThumbnail.objects.all()
    serializer_class = serializers.VideoThumbnailSerializer
