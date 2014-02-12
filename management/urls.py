from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from .views import *

urlpatterns = patterns('',
    url(r'^$', homepage.as_view(), name='coach_portal'),
)