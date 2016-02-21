from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.forms import ModelForm, modelform_factory
from .models import Team, Match
from forms import MatchForm
from django.views.generic import View


def get_name(request):
    TeamForm = modelform_factory(Team, fields='__all__')
    if request.method == 'POST':
        team_form = TeamForm(request.POST, request.FILES)
        if team_form.is_valid():
            team_form.save()
            return render(
                request,
                'confirmation.html',
                {
                    'team_form': team_form,
                }
            )
    else:
        team_form = TeamForm()
    return render(
        request,
        'team_info.html',
        {
            'team_form': team_form,
        }
    )


def get_match(request):
    match_form = modelform_factory(Match, fields='__all__')
    if request.method == 'POST':
        match_form = MatchForm(request.POST, request.FILES)
        if match_form.is_valid():
            match_form.save()
            return render(
                request,
                'confirmation.html',
                {
                    'match_form': match_form
                }
            )
    else:
        match_form = MatchForm()
    return render(
        request,
        'match.html',
        {
            'match_form': match_form
        }
    )

def team_stats_from_team_number(request, team_number):
    team = get_object_or_404(Team, team_number=team_number)
    print(team_number)
    # team_number is the variable that will now allow you to do all the things
    return render(request, 'team-stats.html', {'teams': team.team_number})
