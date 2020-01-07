# yelp/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import index
from .views import YelpYelpScrapingCreateView
from .views import YelpYelpScrapingDetailsView

urlpatterns = {
    url(r'^yelp/index/$', index, name='index'),
    url(r'^yelp/$', 
        YelpYelpScrapingCreateView.as_view(), name="create"),
    url(r'^yelp/(?P<pk>[0-9a-f-]+)/$',
        YelpYelpScrapingDetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)