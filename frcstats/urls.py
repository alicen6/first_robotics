from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.contrib import admin
from .views import (get_name, get_match, team_stats, get_home, get_thanks,
                    team_stats_from_team_number, battle_match, team_raw_stats,
                    team_raw_from_team_number, get_extra, team_compare,
                    team_compare_info, event_info, teams_by_event,
                    alliance_select)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^form/team_info/$', get_name.get_name),
    url(r'^form/match/$', get_match.get_match, name='match'),
    url(r'^login/$', auth_views.login),
    url(r'^team-stats/$', team_stats.team_stats, name='team-stats'),
    url(r'^team-stats/(?P<team_number>[0-9]+)/$',
        team_stats_from_team_number.team_stats_from_team_number, name='team-test'),
    url(r'^team-raw-stats/$', team_raw_stats.team_raw_stats, name='team-raw-stats'),
    url(r'^team-raw-stats/(?P<team_number>[0-9]+)/$',
        team_raw_from_team_number.team_raw_from_team_number, name='team-raw'),
    url(r'^home/', get_home.get_home, name='home'),
    url(r'^thanks/', get_thanks.get_thanks, name='thanks'),
    url(r'^drive/', get_extra.get_extra, name='drive'),
    url(r'^team-compare/$', team_compare.team_compare, name='team-compare'),
    url(r'^team-compare/(?P<first_team>[0-9]+)/(?P<second_team>[0-9]+)/$',
        team_compare_info.team_compare_info, name='team-compare-info'),
    url(r'^event-info/$', event_info.event_info, name='event-select'),
    url(r'^event-info/(?P<shorthand>.+)/$',
        teams_by_event.teams_by_event, name='event-info'),
    url(r'^alliance-select/$', alliance_select.alliance_select, name='alliance-select'),
    url(r'^alliance-select/(?P<red_one>[0-9]+)/(?P<red_two>[0-9]+)/(?P<red_three>[0-9]+)_(?P<blue_one>[0-9]+)/(?P<blue_two>[0-9]+)/(?P<blue_three>[0-9]+)/$',
        battle_match.battle_match, name='battle-match-results'),
]
