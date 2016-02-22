from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.forms import ModelForm, modelform_factory
from .models import Team, Match
from forms import MatchForm
from django.views.generic import View
from django import forms
from .choices import auton_def_choices


def get_name(request):
    TeamForm = modelform_factory(Team, fields='__all__')
    if request.method == 'POST':
        team_form = Team(request.POST, request.FILES)
        if team_form.is_valid():
            team_form.save()
            return render(request, 'confirmation.html', {'team_form': team_form, })
    else:
        team_form = TeamForm()
    return render(request, 'team_info.html', {'team_form': team_form})


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


def team_stats(request):
    class TeamNumberForm(forms.Form):
        team_number = forms.IntegerField()
    if request.method == 'GET':
        form = TeamNumberForm()
    else:
        # A POST request: Handle Form Upload
        form = TeamNumberForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            team_number = form.cleaned_data['team_number']
            return HttpResponseRedirect('/team-stats/' + str(team_number))
    return render(request, 'team_number.html', {'team_number_form': form})


def team_stats_from_team_number(request, team_number):
    team = Team.objects.filter(team_number=team_number)
    matches = Match.objects.filter(team_number=team[0].id)
    auton_low_values = []
    auton_high_values = []
    auton_def_reached_values = []
    auton_def_crossed_values = []
    teleop_low_values = []
    teleop_high_values = []
    hang_input_values = []
    hang_success_values = []
    hang_fail_values = []
    played_def_values = []
    portc_stats = []
    portc_stuck_stats = []
    drawb_stats = []
    drawb_stuck_stats = []
    cdf_stats = []
    cdf_stuck_stats = []
    moat_stats = []
    moat_stuck_stats = []
    sallyp_stats = []
    sallyp_stuck_stats = []
    rought_stats = []
    rought_stuck_stats = []
    lowbar_stats = []
    lowbar_stuck_stats = []
    ramparts_stats = []
    ramparts_stuck_stats = []
    for match in matches:
        if match.teleop_portc == 1:
            portc_stuck_stats.append(match.teleop_portc)
        elif match.teleop_portc != 0:
            portc_stats.append(match.teleop_portc)
        else:
            pass
        if match.teleop_drawb == 1:
            drawb_stuck_stats.append(match.teleop_drawb)
        elif match.teleop_drawb != 0:
            drawb_stats.append(match.teleop_drawb)
        else:
            pass
        if match.teleop_cdf == 1:
            cdf_stuck_stats.append(match.teleop_cdf)
        elif match.teleop_cdf != 0:
            cdf_stats.append(match.teleop_cdf)
        else:
            pass
        if match.teleop_moat == 1:
            moat_stuck_stats.append(match.teleop_moat)
        elif match.teleop_moat != 0:
            moat_stats.append(match.teleop_moat)
        else:
            pass
        if match.teleop_sallyp == 1:
            sallyp_stuck_stats.append(match.teleop_sallyp)
        elif match.teleop_sallyp != 0:
            sallyp_stats.append(match.teleop_sallyp)
        else:
            pass
        if match.teleop_rought == 1:
            rought_stuck_stats.append(match.teleop_rought)
        elif match.teleop_rought != 0:
            rought_stats.append(match.teleop_rought)
        else:
            pass
        if match.teleop_lowbar == 1:
            lowbar_stuck_stats.append(match.teleop_lowbar)
        elif match.teleop_lowbar != 0:
            lowbar_stats.append(match.teleop_lowbar)
        else:
            pass
        if match.teleop_ramparts == 1:
            ramparts_stuck_stats.append(match.teleop_ramparts)
        elif match.teleop_ramparts != 0:
            ramparts_stats.append(match.teleop_ramparts)
        else:
            pass
        if match.hang_input == 1:
            hang_input_values.append(match.hang_input)
        elif match.hang_input == 2:
            hang_success_values.append(match.hang_input)
        else:
            hang_fail_values.append(match.hang_input)

        auton_low_values.append(match.auton_low_goals)
        auton_high_values.append(match.auton_high_goals)
        teleop_low_values.append(match.teleop_low_goals)
        teleop_high_values.append(match.teleop_high_goals)
        auton_def_reached_values.append(match.auton_def_reached)
        auton_def_crossed_values.append(match.auton_def_crossed)
        played_def_values.append(match.played_def)
        auton_low_stats = sum(auton_low_values) / float(len(auton_low_values))
        auton_high_stats = sum(auton_high_values) / \
            float(len(auton_high_values))
    teleop_low_stats = sum(teleop_low_values) / float(len(teleop_low_values))
    teleop_high_stats = sum(teleop_high_values) / \
        float(len(teleop_high_values))
    portc_stats_value = (sum(portc_stats) -
                         float(len(portc_stats))) / float(len(portc_stats)) if len(portc_stats) != 0 else 0
    portc_stuck_stats = str(int(((float(len(portc_stuck_stats)) /
                                  (float(len(portc_stats))) if len(portc_stats) != 0 else 0) + float(len(portc_stuck_stats))) * 100)) + "%"
    drawb_stats_value = (sum(drawb_stats) -
                         float(len(drawb_stats))) / float(len(drawb_stats)) if len(drawb_stats) != 0 else 0
    drawb_stuck_stats = str(int(((float(len(drawb_stuck_stats)) /
                                  (float(len(drawb_stats))) if len(drawb_stats) != 0 else 0) + float(len(drawb_stuck_stats))) * 100)) + "%"
    cdf_stats_value = (sum(cdf_stats) - float(len(cdf_stats))
                       ) / float(len(cdf_stats)) if len(cdf_stats) != 0 else 0
    cdf_stuck_stats = str(int(((float(len(cdf_stuck_stats)) /
                                     (float(len(cdf_stats))) if len(cdf_stats) != 0 else 0) + float(len(cdf_stuck_stats))) * 100)) + "%"
    moat_stats_value = (sum(moat_stats) - float(len(moat_stats))
                        ) / float(len(moat_stats)) if len(moat_stats) != 0 else 0
    moat_stuck_stats = str(int(((float(len(moat_stuck_stats)) /
                                 (float(len(moat_stats))) if len(moat_stats) != 0 else 0) + float(len(moat_stuck_stats))) * 100)) + "%"
    sallyp_stats_value = (sum(sallyp_stats) - float(len(sallyp_stats))
                          ) / float(len(sallyp_stats)) if len(sallyp_stats) != 0 else 0
    sallyp_stuck_stats = str(int(((float(len(sallyp_stuck_stats)) /
                                   (float(len(sallyp_stats))) if len(sallyp_stats) != 0 else 0) + float(len(sallyp_stuck_stats))) * 100)) + "%"
    rought_stats_value = (sum(rought_stats) - float(len(rought_stats))
                          ) / float(len(rought_stats)) if len(rought_stats) != 0 else 0
    rought_stuck_stats = str(int(((float(len(rought_stuck_stats)) /
                                   (float(len(rought_stats))) if len(rought_stats) != 0 else 0) + float(len(rought_stuck_stats))) * 100)) + "%"
    lowbar_stats_value = (sum(lowbar_stats) - float(len(lowbar_stats))
                          ) / float(len(lowbar_stats)) if len(lowbar_stats) != 0 else 0
    lowbar_stuck_stats = str(int(((float(len(lowbar_stuck_stats)) /
                                   (float(len(lowbar_stats))) if len(lowbar_stats) != 0 else 0) + float(len(lowbar_stuck_stats))) * 100)) + "%"
    ramparts_stats_value = (sum(ramparts_stats) - float(len(ramparts_stats))
                            ) / float(len(ramparts_stats)) if len(ramparts_stats) != 0 else 0
    ramparts_stuck_stats = str(int(((float(len(ramparts_stuck_stats)) /
                                     (float(len(ramparts_stats))) if len(ramparts_stats) != 0 else 0) + float(len(ramparts_stuck_stats))) * 100)) + "%"
    hang_value = str(
        int(((float(len(hang_input_values)) + float(len(hang_success_values))) /
             (float(len(hang_input_values)) + float(len(hang_success_values)) + float(len(hang_fail_values)))) * 100)) + "%"
    hang_success_stats = str(int(float(len(hang_success_values)) / (
        float(len(hang_input_values)) + float(len(hang_success_values))) * 100)) + "%"
    hang_fail = str(int((float(len(hang_fail_values)) /
                         float(len(hang_input_values) + len(hang_fail_values))) * 100)) + "%"
    played_def_stats = str(
        int((sum(played_def_values) / float(len(played_def_values))) * 100)) + "%"

    # team = get_object_or_404(Team, team_number=team_number)
    # team_number is the variable that will now allow you to do all the things
    """
    l = [["hi", "there"], ["hello", "their"]]
    [x[0] for x in l]
    for x in l:
        print x[0]

    d = {"hi": "there", "hello": "their"}
    {x for x in d}
    for x, y in d.iteritems():
        print x, y
    """
    return render(request, 'team-stats.html', {'teams': team,
                                               'hang_value': hang_value, 'hang_fail': hang_fail,
                                               'auton_low_stats': auton_low_stats,
                                               'auton_high_stats': auton_high_stats,
                                               'teleop_low_stats': teleop_low_stats,
                                               'teleop_high_stats': teleop_high_stats,
                                               'auton_def_reached_values': list({auton_def_choices[x] for x in auton_def_reached_values}),
                                               'auton_def_crossed_values': list({auton_def_choices[x] for x in auton_def_crossed_values}),
                                               'played_def_stats': played_def_stats,
                                               'portc_stats_value': portc_stats_value,
                                               'portc_stuck_stats': portc_stuck_stats,
                                               'drawb_stats_value': drawb_stats_value,
                                               'drawb_stuck_stats': drawb_stuck_stats,
                                               'cdf_stats_value': cdf_stats_value,
                                               'cdf_stuck_stats': cdf_stuck_stats,
                                               'moat_stats_value': moat_stats_value,
                                               'moat_stuck_stats': moat_stuck_stats,
                                               'sallyp_stats_value': sallyp_stats_value,
                                               'sallyp_stuck_stats': sallyp_stuck_stats,
                                               'rought_stats_value': rought_stats_value,
                                               'rought_stuck_stats': rought_stuck_stats,
                                               'lowbar_stats_value': lowbar_stats_value,
                                               'lowbar_stuck_stats': lowbar_stuck_stats,
                                               'ramparts_stats_value': ramparts_stats_value,
                                               'ramparts_stuck_stats': ramparts_stuck_stats,
                                               'hang_success_stats': hang_success_stats
                                               })
