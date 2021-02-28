import requests
from content.models import Video, VideoThumbnail


class YoutubeService(object):
    q = 'dogs'
    api_key = 'AIzaSyAWVS_vmOTMJgpc8OHqsMHo4Uc27_tMzXo'
    url = "https://youtube.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=50&order=date&publishedAfter={publishedAfter}&key={api_key}&q={q}"

    @classmethod
    def get_videos_from_youtube(cls, iso_time):
        payload = {}
        headers = {
            'Accept': 'application/json'
        }
        response = requests.request(
            "GET",
            cls.url.format(
                api_key=cls.api_key,
                publishedAfter=iso_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
                q=cls.q
            ),
            headers=headers,
            data=payload
        )
        videos_json = response.json().get('items', [])
        return videos_json

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
