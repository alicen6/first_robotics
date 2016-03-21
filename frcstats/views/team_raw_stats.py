from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.forms import ModelForm, modelform_factory
from frcstats.models import Team
from django.views.generic import View
from django import forms
from django.db import connection


def team_raw_stats(request):
    class TeamNumberForm(forms.Form):
        team_number = forms.IntegerField()
    if request.method == 'GET':
        form = TeamNumberForm()
    else:
        # A POST request: Handle Form Upload
        form = TeamNumberForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            team_number = abs(form.cleaned_data['team_number'])
            return HttpResponseRedirect('/team-raw-stats/' + str(team_number))
    return render(request, 'team_number.html', {'team_number_form': form})
