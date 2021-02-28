from django.utils import timezone
from haystack import indexes
from app.content.models import Video


class VideoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="title")
    description = indexes.CharField(model_attr="description")
    created_on = indexes.DateTimeField(model_attr="created_on")
    modified_at = indexes.DateTimeField(model_attr="modified_at")

    def get_model(self):
        return Video

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(
            created__lte=timezone.now()
        )
