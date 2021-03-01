from rest_framework import serializers
from . import models


class YoutubeAPIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.YoutubeAPIKey
        fields = ('id', 'api_key', 'status')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = ('youtube_id', 'title', 'description')


class VideoThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VideoThumbnail
        fields = ('url')
