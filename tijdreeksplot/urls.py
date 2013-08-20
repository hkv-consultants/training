from django.conf.urls import patterns, url
from .views import location_list, LocationDetail


urlpatterns = patterns('',
    url(r'^locations/$', location_list),
    url(r'^locations/(?P<slug>[\w-]+)/$', LocationDetail.as_view(), name='location-detail'),
)