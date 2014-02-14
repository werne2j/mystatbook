from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from .views import *

urlpatterns = patterns('',
    url(r'^(?P<username>\w+)/$', Homepage.as_view(), name='coach_portal'),
)