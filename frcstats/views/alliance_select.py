from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from frcstats.models import Team
from django.views.generic import View
from django import forms
from django.db import connection


def alliance_select(request):
    class TeamNumberForm(forms.Form):
        red_one = forms.IntegerField()
        red_two = forms.IntegerField()
        red_three = forms.IntegerField()
        blue_one = forms.IntegerField()
        blue_two = forms.IntegerField()
        blue_three = forms.IntegerField()
    if request.method == 'GET':
        form = TeamNumberForm()
    else:
        form = TeamNumberForm(request.POST)
        if form.is_valid():
            red_one = abs(form.cleaned_data['red_one'])
            red_two = abs(form.cleaned_data['red_two'])
            red_three = abs(form.cleaned_data['red_three'])
            blue_one = abs(form.cleaned_data['blue_one'])
            blue_two = abs(form.cleaned_data['blue_two'])
            blue_three = abs(form.cleaned_data['blue_three'])
            return HttpResponseRedirect('/alliance-select/' + str(red_one) + "/" + str(red_two) + "/" + str(red_three) + "_" + str(blue_one) + "/" + str(blue_two) + "/" + str(blue_three))
    return render(request, 'alliance-select.html', {'team_number_form': form})
