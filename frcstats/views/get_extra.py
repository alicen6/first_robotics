from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.forms import ModelForm, modelform_factory
from frcstats.models import Team, Drive
from frcstats.forms import DriveForm
from django.views.generic import View
from django import forms
from django.db import connection


def get_extra(request):
    drive_form = modelform_factory(Drive, fields='__all__')
    if request.method == 'POST':
        drive_form = DriveForm(request.POST, request.FILES)
        if drive_form.is_valid():
            team_number = drive_form.cleaned_data['team_number']
            drivetrain = drive_form.cleaned_data['drivetrain']
            gear_reduc = drive_form.cleaned_data['gear_reduc']
            motors = drive_form.cleaned_data['motors']
            extra_notes = drive_form.cleaned_data['extra_notes']
            existing_drive_data = Drive.objects.filter(team_number=team_number).update(
                drivetrain=drivetrain,
                gear_reduc=gear_reduc,
                motors=motors,
                extra_notes=extra_notes)
            if not existing_drive_data:
                drive_form.save()
            return render(request, 'confirmation.html', {'drive_form': drive_form})
        else:
            print drive_form.errors
    else:
        drive_form = DriveForm()
    return render(request, 'drive.html', {'drive_form': drive_form})
