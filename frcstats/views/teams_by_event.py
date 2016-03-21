from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from frcstats.models import TeamsByEvent, Event
from django.views.generic import View
from django.db import connection


def teams_by_event(request, shorthand):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT event_name, team_number
            FROM teams_by_event
            WHERE team_number IN (
                SELECT team_number FROM teams_by_event
                    WHERE shorthand = %s)
            ORDER BY team_number
    """, [shorthand])
    event_team = cursor.fetchall()
    cursor.close()
    # print event_team
    # results = TeamsByEvent.objects.raw(raw_query)
    # print results
    return render(request, 'event-info.html', {'events_and_teams': event_team})
