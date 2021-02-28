from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path(r'^search/', include('search.urls')),
]
