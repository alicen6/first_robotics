from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.forms import ModelForm, modelform_factory
from .models import Team, Match
from forms import MatchForm
from django.views.generic import View
from django import forms


def get_name(request):
    TeamForm = modelform_factory(Team, fields='__all__')
    if request.method == 'POST':
        team_form = Team(request.POST, request.FILES)
        if team_form.is_valid():
            team_form.save()
            return render(request, 'confirmation.html', {'team_form': team_form,})
    else:
        team_form = TeamForm()
    return render(request, 'team_info.html', {'team_form': team_form})


def get_match(request):
    match_form = modelform_factory(Match, fields='__all__')
    if request.method == 'POST':
        match_form = MatchForm(request.POST, request.FILES)
        if match_form.is_valid():
            match_form.save()
            return render(request, 'confirmation.html', {'match_form': match_form})
    else:
        match_form = MatchForm()
    return render(request, 'match.html', {'match_form': match_form})


def team_stats(request):
    class TeamNumberForm(forms.Form):
        team_number = forms.IntegerField()
    if request.method == 'GET':
        form = TeamNumberForm()
    else:
        # A POST request: Handle Form Upload
        form = TeamNumberForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            team_number = form.cleaned_data['team_number']
            return HttpResponseRedirect('/team-stats/' + str(team_number))
    return render(request, 'team_number.html', {'team_number_form': form})


def team_stats_from_team_number(request, team_number):
    team = Team.objects.filter(team_number=team_number)
    matches = Match.objects.filter(team_number=team[0].id)
    #team = get_object_or_404(Team, team_number=team_number)
    # team_number is the variable that will now allow you to do all the things
    return render(request, 'team-stats.html', {'teams': team, 'matches': matches})
