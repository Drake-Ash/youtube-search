from django.utils import timezone
from haystack import indexes
from content.models import Video


class VideoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="title")
    description = indexes.CharField(model_attr="description")
    published_after = indexes.DateTimeField(model_attr="published_after")

    def get_model(self):
        return Video

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(
            published_after__lte=timezone.now()
        )
