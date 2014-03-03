from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from .views import *

urlpatterns = patterns('',
    url(r'^(?P<username>\w+)/$', Homepage.as_view(), name='coach_portal'),
    url(r'^(?P<username>\w+)/add_team/$', AddTeam.as_view(), name='add_team'),
    url(r'^(?P<username>\w+)/(?P<name>\w+)/(?P<year>\w+)/$', SeasonDetail.as_view(), name='season_detail'),
    url(r'^(?P<username>\w+)/(?P<name>\w+)/(?P<year>\w+)/player_list/$', PlayerList.as_view(), name='player_list'),
    url(r'^(?P<username>\w+)/(?P<name>\w+)/(?P<year>\w+)/game_list/$', GameList.as_view(), name='game_list'),
    url(r'^(?P<username>\w+)/(?P<name>\w+)/(?P<year>\w+)/player_stats/$', PlayerStats.as_view(), name='player_stats'),
    url(r'^(?P<username>\w+)/(?P<name>\w+)/(?P<year>\w+)/depth_chart/$', Depth_Chart.as_view(), name='depth_chart'),
)