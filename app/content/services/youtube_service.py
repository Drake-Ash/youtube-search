import requests
from content.models import *
from django.utils import timezone
from datetime import timedelta


class YoutubeService(object):
    q = 'dogs'
    api_keys = []
    url = "https://youtube.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=50&order=date&publishedAfter={publishedAfter}&key={api_key}&q={q}"

    @classmethod
    def create_or_update_videos(cls, videos_json):
        for video_json in videos_json:
            video_dict, thumbnails = cls.get_video_dict(video_json)
            video, _ = Video.objects.update_or_create(**video_dict)
            video_thumbnails = []
            for thumbnail in thumbnails:
                video_thumbnails.append(VideoThumbnail.objects.create(url=thumbnail))
            video.thumbnail_urls.set(video_thumbnails)
            video.save()

    @classmethod
    def get_video_dict(cls, video_json):
        video = {
            'youtube_id': video_json['id']['videoId'],
            'title': video_json['snippet']['title'],
            'description': video_json['snippet']['description'],
            'published_after': video_json['snippet']['publishedAt']
        }
        thumbnails = []
        for key, thumbnail in video_json['snippet']['thumbnails'].items():
            thumbnails.append(thumbnail['url'])
        return video, thumbnails

    @classmethod
    def set_api_key_status(cls, status, api_key):
        YoutubeAPIKey.objects.filter(api_key=api_key).update(status=status)

    @classmethod
    def set_active_api_keys(cls):
        active_api_keys = list(YoutubeAPIKey.objects.filter(status='active').values_list('api_key'))
        if active_api_keys:
            cls.api_keys = active_api_keys
            return

    @classmethod
    def set_quota_reusable_api_keys(cls):
        yesterday = timezone.now() - timedelta(days=1)
        quota_renewed_api_keys = list(
            YoutubeAPIKey.objects.filter(
                status='expired',
                modified_at__lt=yesterday
            ).order_by('modified_at').values_list('api_key')
        )

        if quota_renewed_api_keys:
            cls.api_keys = quota_renewed_api_keys

    @classmethod
    def set_api_keys(cls):
        cls.set_active_api_keys()
        if not cls.api_keys:
            cls.set_quota_reusable_api_keys()
        if not cls.api_keys:
            raise Exception('All keys expired, please add new key')

    @classmethod
    def get_next_api_key(cls):
        if len(cls.api_keys) != 0 and not cls.check_for_usable_keys():
            raise Exception('All keys expired, please add new key')

        if len(cls.api_keys) == 0:
            cls.set_api_keys()

        api_key = cls.api_keys[0]
        cls.set_api_key_status('expired', api_key)
        cls.api_keys = cls.api_keys[1:]

        if len(cls.api_keys) > 0:
            return cls.api_keys[0]
        else:
            raise Exception('All keys expired, please add new key')

    @classmethod
    def check_for_usable_keys(cls):
        yesterday = timezone.now() - timedelta(days=1)
        reusable_key_exists = YoutubeAPIKey.objects.filter(status='expired', modified_at__lt=yesterday).exists()
        active_key_exists = YoutubeAPIKey.objects.filter(status='active').exists()
        return True if reusable_key_exists or active_key_exists else False

    @classmethod
    def get_videos_from_youtube(cls, iso_time):
        if not cls.check_for_usable_keys():
            raise Exception('All keys expired, please add new key')

        if not cls.api_keys:
            cls.set_api_keys()

        result = None
        api_key = cls.api_keys[0]
        videos_json = []
        while not result:
            if not api_key:
                api_key = cls.get_next_api_key()
            response = cls.get_videos_from_youtube_api(api_key, iso_time)

            if response.status_code != 200:
                api_key = None
                continue

            result = response.json()
            print(response.text)
            videos_json = result.get('items', [])

        return videos_json

    @classmethod
    def get_videos_from_youtube_api(cls, api_key, iso_time):
        payload = {}
        headers = {
            'Accept': 'application/json'
        }
        response = requests.request(
            "GET",
            cls.url.format(
                api_key=api_key,
                publishedAfter=iso_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
                q=cls.q
            ),
            headers=headers,
            data=payload
        )
        return response
