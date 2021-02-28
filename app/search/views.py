from drf_haystack.serializers import HaystackSerializer
from drf_haystack.viewsets import HaystackViewSet

from .models import Video
from .search_indexes import VideoIndex


class VideoSerializer(HaystackSerializer):

    class Meta:
        # The `index_classes` attribute is a list of which search indexes
        # we want to include in the search.
        index_classes = [VideoIndex]

        # The `fields` contains all the fields we want to include.
        # NOTE: Make sure you don't confuse these with model attributes. These
        # fields belong to the search index!
        fields = [
            "text", "title", "description"
        ]


class VideoSearchView(HaystackViewSet):

    # `index_models` is an optional list of which models you would like to include
    # in the search result. You might have several models indexed, and this provides
    # a way to filter out those of no interest for this particular view.
    # (Translates to `SearchQuerySet().models(*index_models)` behind the scenes.
    index_models = [Video]

    serializer_class = VideoSerializer
