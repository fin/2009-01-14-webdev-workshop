from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^projectvault/', include('projectvault.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    (r'^$', direct_to_template, {'template': 'index.html'}),
    (r'^who/$', direct_to_template, {'template': 'author/list.html'}),
    (r'^who/leo/$', direct_to_template, {'template': 'project/list.html'}),
    (r'^who/leo/project1/$', direct_to_template, {'template': 'project/detail.html'}),


    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
