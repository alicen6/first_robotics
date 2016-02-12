from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import *
from .models import Team


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Team(request.POST)
        match = Match(request.POST)
        auto = Autonomous(request.POST)
        teleop = Teleoperated(request.POST)
        # check whether it's valid:
        if form.is_valid() and auto.is_valid() and match.is_valid() and teleop.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Team()
        auto = Autonomous()
        match = Match()
        teleop = Teleoperated()

    return render(request, 'name.html', {'form': form, 'auto': auto,
    'match': match, 'teleop': teleop, })
