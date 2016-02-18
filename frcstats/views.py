from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm, modelform_factory
from .models import Team, Match
from forms import MatchForm


def get_name(request):
    TeamForm = modelform_factory(Team, fields='__all__')
    if request.method == 'POST':
        team_form = TeamForm(request.POST, request.FILES)
        if team_form.is_valid():
            team_form.save()
            return render(
                request,
                'confirmation.html',
                {
                    'team_form': team_form,
                }
            )
    else:
        team_form = TeamForm()
    return render(
        request,
        'team_info.html',
        {
            'team_form': team_form,
        }
    )


def get_match(request):
    match_form = modelform_factory(Match, fields='__all__')
    if request.method == 'POST':
        match_form = MatchForm(request.POST, request.FILES)
        if match_form.is_valid():
            match_form.save()
            return render(
                request,
                'confirmation.html',
                {
                    'match_form': match_form
                }
            )
    else:
        match_form = MatchForm()
    return render(
        request,
        'match.html',
        {
            'match_form': match_form
        }
    )


# def team_stats(request):
#    team_number = request.GET.get('team_number', '')
#    team_number_stats = Team.objects.filter(team_number=team_number)
#    print team_number
#    return HttpResponse(str(team_number))


# def team_stats(request):
#    stats = TeamStats.objects.filter(team_number=team_number)
#    args = {}
#    args.update(csrf(request))
#    args['team_number'] = team_number
#    if request.method == 'POST':
#        team_number_stats = request.POST.get('team_number_stats')
#        return redirect(reverse('stats_view', args=(team_number_stats,)))
#    else:
#        args = {}
#        args.update(csrf(request))
#        args['team_number'] = team_number
#        return render(request, 'team-stats.html', args)
#
#
# def view_stats(request, team_number_stats):
#    user = User.objects.get(view_stats__id=team_number_stats)
#    site = ProjectSite.objects.get(id=team_number_stats)
#    args = {}
#    args.update(csrf(request))
#    args['Users'] = user
#    args['team_number'] = site
#    return render(request, 'team-stats.html', args)
