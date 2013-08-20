from django.conf.urls import patterns, url
from .views import location_list


urlpatterns = patterns('',
    url(r'^$', location_list),
)