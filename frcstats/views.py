from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.forms import ModelForm, modelformset_factory
from .forms import TeamForm
from .models import Team


def get_name(request):
    TeamFormSet = modelformset_factory(Team, fields=(
        'team_name', 'team_number', 'robot_weight',
        'robot_height', 'team_location', 'team_notes'))
    if request.method == 'POST':
        formset = TeamFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return render(request, 'confirmation.html', {'team_formset': formset})
            # do something.
    else:
        formset = TeamFormSet()
    return render(request, 'name.html', {'team_formset': formset})
