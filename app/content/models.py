from django.db import models


class Video(models.Model):
    youtube_id = models.TextField(db_index=True, unique=True, primary_key=True)
    title = models.TextField(db_index=True)
    description = models.TextField(db_index=True)
    thumbnail_urls = models.ManyToManyField('VideoThumbnail', blank=True, null=True)
    published_after = models.DateTimeField(db_index=True, default=None)


class VideoThumbnail(models.Model):
    url = models.URLField(db_index=True)


class YoutubeAPIKey(models.Model):
    api_key = models.TextField(db_index=True)
    status = models.CharField(max_length=50, db_index=True, default='active')
    modified_at = models.DateTimeField(db_index=True, auto_now=True)
