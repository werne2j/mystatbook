from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib.auth.views import password_change
from django.core.urlresolvers import reverse_lazy
from .views import *

urlpatterns = patterns('',
    url(r'^(?P<username>\w+)/$', Homepage.as_view(), name='coach_portal'),
    url(r'^(?P<username>\w+)/settings$', Settings.as_view(), name='user_settings'),
    url(r'^(?P<username>\w+)/settings/delete/$', DeleteTeam.as_view(), name='delete_team'),
    url(r'^/change_password/$', 'management.views.password_change', name='change_password'),
    url(r'^(?P<username>\w+)/add_team/$', AddTeam.as_view(), name='add_team'),
    url(r'^(?P<username>\w+)/(?P<name>\w+)/add_season/$', AddSeason.as_view(), name='add_season'),
    url(r'^(?P<username>\w+)/(?P<name>\w+)/(?P<year>\w+)/$', SeasonDetail.as_view(), name='season_detail'),
    url(r'^(?P<username>\w+)/(?P<name>\w+)/(?P<year>\w+)/player_list/$', PlayerList.as_view(), name='player_list'),
    url(r'^(?P<username>\w+)/(?P<name>\w+)/(?P<year>\w+)/game_list/$', GameList.as_view(), name='game_list'),
    url(r'^(?P<username>\w+)/(?P<name>\w+)/(?P<year>\w+)/player_stats/$', PlayerStats.as_view(), name='player_stats'),
    url(r'^(?P<username>\w+)/(?P<name>\w+)/(?P<year>\w+)/depth_chart/$', Depth_Chart.as_view(), name='depth_chart'),
    url(r'^(?P<username>\w+)/(?P<name>\w+)/(?P<year>\w+)/game/(?P<pk>\w+)/$', GameStats.as_view(), name='game_stats'),
)
