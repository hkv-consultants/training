from django.conf.urls import patterns, url
from .views import location_list, RecordValueListList


urlpatterns = patterns('',
    url(r'^locations/$', location_list),
    url(r'^locations/([\w-]+)/$', RecordValueListList.as_view()),
)