from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.forms import ModelForm, modelform_factory
from frcstats.models import Team, Match, Drive
from frcstats.forms import MatchForm
from django.views.generic import View
from django import forms
from django.db import connection


def get_match(request):
    match_form = modelform_factory(Match, fields='__all__')
    if request.method == 'POST':
        match_form = MatchForm(request.POST, request.FILES)
        if match_form.is_valid():
            match_form.save()
            return render(request, 'confirmation.html', {'match_form': match_form})
        else:
            print match_form.errors
    else:
        match_form = MatchForm()
    return render(request, 'match.html', {'match_form': match_form})
