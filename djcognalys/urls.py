from django.conf.urls import patterns, url
from .views import default_callback

urlpatterns = patterns('',
                       url(r'^call_back/', default_callback)
                       )