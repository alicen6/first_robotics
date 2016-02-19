from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response
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


class TeamStatsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'team-stats.html',
                      {'team_numbers': Team.objects.values('team_number')})

    def post(self, request, *args, **kwargs):
        team_number = TeamStats(request.POST, request.FILES)
        if team_number.is_valid():
            # do stuff & add to database
            team_number.save()
            team_number = TeamStats.objects.create()
            # use my_file.pk or whatever attribute of FileField your id is
            # based on
            return HttpResponseRedirect('/team-stats/%i/' % team_number.pk)
        return render(request, 'team-stats.html', {'team_number': team_number})
