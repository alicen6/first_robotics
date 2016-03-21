from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from frcstats.models import Team
from django.views.generic import View
from django import forms
from django.db import connection


def team_compare(request):
    class TeamNumberForm(forms.Form):
        first_team = forms.IntegerField()
        second_team = forms.IntegerField()
    if request.method == 'GET':
        form = TeamNumberForm()
    else:
        # A POST request: Handle Form Upload
        form = TeamNumberForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            first_team = abs(form.cleaned_data['first_team'])
            second_team = abs(form.cleaned_data['second_team'])
            return HttpResponseRedirect('/team-compare/' + str(first_team) + "/" + str(second_team))
    return render(request, 'team-choice.html', {'team_number_form': form})
