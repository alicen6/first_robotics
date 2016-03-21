from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.forms import ModelForm, modelform_factory
from frcstats.models import TeamsByEvent, Event
from django.views.generic import View
from django import forms
from django.db import connection


def event_info(request):
    class EventForm(forms.Form):
        event_name = forms.CharField()
    if request.method == 'GET':
        form = EventForm()
    else:
        form = EventForm(request.POST)
        if form.is_valid():
            event_name = form.cleaned_data['event_name']
            
            def event_get(event_name):
                s = TeamsByEvent.objects.filter(event_name=event_name)
                return s[0].shorthand
            shorthand = event_get(event_name)
            return HttpResponseRedirect('/event-info/' + str(shorthand))
        else:
            return render(request, 'event-select.html', {'event_form': form})
    return render(request, 'event-select.html', {'event_form': form})
