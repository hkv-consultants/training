from django.conf.urls import patterns, url
from .views import location_list, LocationDetail, RecordValueListDetail


urlpatterns = patterns('',
    url(r'^locations/$', location_list),
    url(r'^locations/(?P<slug>[\w-]+)/$', LocationDetail.as_view(), name='location-detail'),
    url(r'^locations/(?P<location_slug>[\w-]+)/(?P<slug>[\w-]+)/$', RecordValueListDetail.as_view(), name='recordvaluelist-detail'),
)