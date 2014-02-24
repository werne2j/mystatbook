from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from .views import *

urlpatterns = patterns('',
    url(r'^(?P<username>\w+)/$', Homepage.as_view(), name='coach_portal'),
    url(r'^(?P<username>\w+)/(?P<name>\w+)$', TeamDetail.as_view(), name='team_detail'),
    url(r'^(?P<username>\w+)/(?P<name>\w+)/player_list/$', PlayerList.as_view(), name='player_list'),
    url(r'^(?P<username>\w+)/(?P<name>\w+)/game_list/$', GameList.as_view(), name='game_list'),
    url(r'^(?P<username>\w+)/(?P<name>\w+)/player_stats/$', PlayerStats.as_view(), name='player_stats'),
)