from django.db import models


class Video(models.Model):
    youtube_id = models.TextField(db_index=True, unique=True, primary_key=True)
    title = models.TextField(db_index=True)
    description = models.TextField(db_index=True)
    thumbnail_urls = models.ManyToManyField('VideoThumbnail', blank=True, null=True)
    created_on = models.DateTimeField(db_index=True, auto_now_add=True)
    modified_at = models.DateTimeField(db_index=True, auto_now=True)


class VideoThumbnail(models.Model):
    url = models.URLField(db_index=True)
