from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import *
# from .models import Team


def get_name(request):
    # if this is a POST request we need to process the form data
    try:
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            team = TeamForm(request.POST)
            match = MatchForm(request.POST)
            auto = AutonForm(request.POST)
            teleop = TeleopForm(request.POST)
            # check whether it's valid:
            if team.is_valid() and auto.is_valid() and match.is_valid() and teleop.is_valid():
                team.save()
                auto.save()
                match.save()
                teleop.save()
                return HttpResponseRedirect(reverse('frcstats:url'))
            else:
                err_msg = 'Something went wrong.'
                return render(request, 'fail')
    except Exception as error:
        return render(request, error)

    # if a GET (or any other method) we'll create a blank form
    else:
        team = Team()
        auto = Autonomous()
        match = Match()
        teleop = Teleoperated()

    return render(request, 'name.html', {'team': team, 'auto': auto,
    'match': match, 'teleop': teleop, })


# def post_new(request):
#    form = TeamForm()
#    return render(request, 'blog/post_edit.html', {'form': form})
