from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.forms import ModelForm, modelform_factory
from .models import Team, Match
from forms import MatchForm, TeamStats
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


def team_stats(request, team_number):
    TeamForm = modelform_factory(Team, fields='__all__')
    if request.method == 'POST':
        team_form = TeamForm(request.POST, request.FILES)
        if team_form.is_valid():
            choose_team = get_object_or_404(Team, pk=team_number)
            try:
                selected_team = choose_team.team_number.get(
                    pk=request.POST['choice'])
            except (KeyError, Team.DoesNotExist):
                # Redisplay the question voting form.
                return render(request, 'team-stats.html', {
                    'choose_team': choose_team,
                    'error_message': "You didn't select a choice.",
                })
            else:
                selected_team.save()
                # Always return an HttpResponseRedirect after successfully dealing
                # with POST data. This prevents data from being posted twice if a
                # user hits the Back button.
                return HttpResponseRedirect(reverse('team_number:team-stats', args=(choose_team.id,)))
