from django.db import models


class Video(models.Model):
    youtube_id = models.TextField(db_index=True, unique=True, primary_key=True)
    title = models.TextField(db_index=True)
    description = models.TextField(db_index=True)
    thumbnail_urls = models.ManyToManyField('VideoThumbnail', blank=True, null=True)
    published_after = models.DateTimeField(db_index=True, default=None)


class VideoThumbnail(models.Model):
    url = models.URLField(db_index=True)
