"""frcstats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https:
        //docs.djangoproject.com / en / 1.9 / topics / http / urls/
Examples:

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from .views import (
    get_name, get_match, team_stats_from_team_number, team_stats, get_home,
    get_thanks, team_raw_stats, get_extra, team_compare, event_info, teams_by_event,
    alliance_select, battle_match_results)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^form/team_info/$', get_name),
    url(r'^form/match/$', get_match, name='match'),
    url(r'^login/$', auth_views.login),
    url(r'^team-stats/$', team_stats, name='team-stats'),
    url(r'^team-stats/(?P<team_number>[0-9]+)/$',
        views.team_stats_from_team_number, name='team-test'),
    url(r'^team-raw-stats/$', team_raw_stats, name='team-raw-stats'),
    url(r'^team-raw-stats/(?P<team_number>[0-9]+)/$',
        views.team_raw_from_team_number, name='team-raw'),
    url(r'^home/', get_home, name='home'),
    url(r'^thanks/', get_thanks, name='thanks'),
    url(r'^drive/', get_extra, name='drive'),
    url(r'^team-compare/$', team_compare, name='team-compare'),
    url(r'^team-compare/(?P<first_team>[0-9]+)/(?P<second_team>[0-9]+)/$',
        views.team_compare_info, name='team-compare-info'),
    url(r'^event-info/$', event_info, name='event-select'),
    url(r'^event-info/(?P<shorthand>.+)/$',
        views.teams_by_event, name='event-info'),
    url(r'^alliance-select/$', alliance_select, name='alliance-select'),
    url(r'^alliance-select/(?P<red_one>[0-9]+)/(?P<red_two>[0-9]+)/(?P<red_three>[0-9]+)_(?P<blue_one>[0-9]+)/(?P<blue_two>[0-9]+)/(?P<blue_three>[0-9]+)/$',
        views.battle_match_results, name='battle-match-results'),
]
