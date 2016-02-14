from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.forms import ModelForm, modelform_factory
from .models import Team, Match


def get_name(request):
    TeamForm = modelform_factory(Team, fields='__all__')
    MatchForm = modelform_factory(Match, fields='__all__')
    if request.method == 'POST':
        team_form = TeamForm(request.POST, request.FILES)
        match_form = MatchForm(request.POST, request.FILES)
        if team_form.is_valid() and match_form.is_valid():
            team_form.save()
            match_form.save()
            return render(
                request,
                'confirmation.html',
                {
                    'team_form': team_form,
                    'match_form': match_form
                }
            )
    else:
        team_form = TeamForm()
        match_form = MatchForm()
    return render(
        request,
        'form.html',
        {
            'team_form': team_form,
            'match_form': match_form
        }
    )
