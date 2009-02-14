from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    (r'^(?P<username>[^/]+)/$', direct_to_template, {'template': 'project/list.html'}),
    (r'^(?P<username>[^/]+)/(?P<project>[^/]+)/$', direct_to_template, {'template': 'project/list.html'}),
)
