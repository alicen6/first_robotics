from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.forms import ModelForm, modelform_factory
from frcstats.models import Team
from django.views.generic import View
from django import forms
from django.db import connection


def get_name(request):
    TeamForm = modelform_factory(Team, fields='__all__')
    if request.method == 'POST':
        team_form = Team(request.POST, request.FILES)
        if team_form.is_valid():
            team_form.save()
            return render(request, 'confirmation.html', {'team_form': team_form})
    else:
        team_form = TeamForm()
    return render(request, 'team_info.html', {'team_form': team_form})
