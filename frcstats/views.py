from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.forms import ModelForm, modelform_factory
from .models import Team, Match, Drive
from forms import MatchForm, DriveForm
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
            team_number = abs(form.cleaned_data['team_number'])
            return HttpResponseRedirect('/team-stats/' + str(team_number))
    return render(request, 'team_number.html', {'team_number_form': form})


def team_stats_from_team_number(request, team_number):
    def divide(values):
        return (sum(values) - float(len(values))) / float(len(values)) \
            if len(values) != 0 else 0

    def stuck_divide(values, stuck):
        return str(int(((float(len(stuck)) /
                         (float(len(values))) if len(values) != 0 else 0) + float(len(stuck))) * 100)) + "%"
    team = Team.objects.filter(team_number=team_number)
    if len(team) > 0:
        matches = Match.objects.filter(team_number=team[0].id)
        drive = Drive.objects.filter(team_number=team[0].id)
        drivetrain = []
        gear_reduc = []
        motors = []
        notes = []
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
        rockwall_stats = []
        rockwall_stuck_stats = []
        try:
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
                if match.teleop_rockwall == 1:
                    rockwall_stuck_stats.append(match.teleop_rockwall)
                elif match.teleop_rockwall != 0:
                    rockwall_stats.append(match.teleop_rockwall)
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
                auton_low_stats = sum(auton_low_values) / \
                    float(len(auton_low_values))
                auton_high_stats = sum(auton_high_values) / \
                    float(len(auton_high_values))
            teleop_low_stats = sum(teleop_low_values) / \
                float(len(teleop_low_values))
            teleop_high_stats = sum(teleop_high_values) / \
                float(len(teleop_high_values))
            portc_stats_value = divide(portc_stats)
            portc_stuck_stats = stuck_divide(portc_stats, portc_stuck_stats)
            drawb_stats_value = divide(drawb_stats)
            drawb_stuck_stats = stuck_divide(drawb_stats, drawb_stuck_stats)
            cdf_stats_value = divide(cdf_stats)
            cdf_stuck_stats = stuck_divide(cdf_stats, cdf_stuck_stats)
            moat_stats_value = divide(moat_stats)
            moat_stuck_stats = stuck_divide(moat_stats, moat_stuck_stats)
            sallyp_stats_value = divide(sallyp_stats)
            sallyp_stuck_stats = stuck_divide(sallyp_stats, sallyp_stuck_stats)
            rought_stats_value = divide(rought_stats)
            rought_stuck_stats = stuck_divide(rought_stats, rought_stuck_stats)
            lowbar_stats_value = divide(lowbar_stats)
            lowbar_stuck_stats = stuck_divide(lowbar_stats, lowbar_stuck_stats)
            ramparts_stats_value = divide(ramparts_stats)
            ramparts_stuck_stats = stuck_divide(
                ramparts_stats, ramparts_stuck_stats)
            rockwall_stats_value = divide(rockwall_stats)
            rockwall_stuck_stats = stuck_divide(
                rockwall_stats, rockwall_stuck_stats)
            hang_value = str(
                int(((float(len(hang_input_values)) + float(len(hang_success_values))) /
                     (float(len(hang_input_values)) + float(len(hang_success_values)) + float(len(hang_fail_values)))) * 100)) + "%"
            hang_success_stats = str(int(float(len(hang_success_values)) / (
                float(len(hang_input_values)) + float(len(hang_success_values))) * 100)) + "%"
            hang_fail = str(int((float(len(hang_fail_values)) /
                                 float(len(hang_input_values) + len(hang_fail_values))) * 100)) + "%"
            played_def_stats = str(
                int((sum(played_def_values) / float(len(played_def_values))) * 100)) + "%"
            for entry in drive:
                drivetrain.append(entry.drivetrain)
                gear_reduc.append(entry.gear_reduc)
                motors.append(entry.motors)
                notes.append(entry.extra_notes)

            # team = get_object_or_404(Team, team_number=team_number)
            # team_number is the variable that will now allow you to do all the
            # things
            return render(request, 'team-stats.html', {
                'teams': team,
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
                'rockwall_stats_value': rockwall_stats_value,
                'rockwall_stuck_stats': rockwall_stuck_stats,
                'hang_success_stats': hang_success_stats,
                'drivetrain': drivetrain,
                'gear_reduc': gear_reduc,
                'motors': motors,
                'notes': notes
            }
            )
        except:
            context = {}
            return render(request, 'no-team.html', context)
    else:
        context = {}
        return render(request, 'non-team.html', context)


def get_home(request):
    context = {}
    return render(request, 'home.html', context)


def get_thanks(request):
    context = {}
    return render(request, 'thanks.html', context)


def team_raw_stats(request):
    class TeamNumberForm(forms.Form):
        team_number = forms.IntegerField()
    if request.method == 'GET':
        form = TeamNumberForm()
    else:
        # A POST request: Handle Form Upload
        form = TeamNumberForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            team_number = abs(form.cleaned_data['team_number'])
            return HttpResponseRedirect('/team-raw-stats/' + str(team_number))
    return render(request, 'team_number.html', {'team_number_form': form})


def team_raw_from_team_number(request, team_number):
    team = Team.objects.filter(team_number=team_number)
    if len(team) > 0:
        matches = Match.objects.filter(team_number=team[0].id)
        auton_low_values = []
        auton_high_values = []
        auton_def_reached_values = []
        auton_def_crossed_values = []
        teleop_low_values = []
        teleop_high_values = []
        hang_input_values = []
        played_def_values = []
        portc_stats = []
        drawb_stats = []
        cdf_stats = []
        moat_stats = []
        sallyp_stats = []
        rought_stats = []
        lowbar_stats = []
        ramparts_stats = []
        rockwall_stats = []
        match_number = []
        try:
            for match in matches:
                if match.teleop_portc == 1:
                    portc_stats.append('got stuck')
                elif match.teleop_portc == 2:
                    portc_stats.append('crossed once')
                elif match.teleop_portc == 3:
                    portc_stats.append('crossed twice')
                else:
                    portc_stats.append('not in play')
                if match.teleop_drawb == 1:
                    drawb_stats.append('got stuck')
                elif match.teleop_drawb == 2:
                    drawb_stats.append('crossed once')
                elif match.teleop_drawb == 3:
                    drawb_stats.append('crossed twice')
                else:
                    drawb_stats.append('not in play')
                if match.teleop_cdf == 1:
                    cdf_stats.append('got stuck')
                elif match.teleop_cdf == 2:
                    cdf_stats.append('crossed once')
                elif match.teleop_cdf == 3:
                    cdf_stats.append('crossed twice')
                else:
                    cdf_stats.append('not in play')
                if match.teleop_moat == 1:
                    moat_stats.append('got stuck')
                elif match.teleop_moat == 2:
                    moat_stats.append('crossed once')
                elif match.teleop_moat == 3:
                    moat_stats.append('crossed twice')
                else:
                    moat_stats.append('not in play')
                if match.teleop_sallyp == 1:
                    sallyp_stats.append('got stuck')
                elif match.teleop_sallyp == 2:
                    sallyp_stats.append('crossed once')
                elif match.teleop_sallyp == 3:
                    sallyp_stats.append('crossed twice')
                else:
                    sallyp_stats.append('not in play')
                if match.teleop_rought == 1:
                    rought_stats.append('got stuck')
                elif match.teleop_rought == 2:
                    rought_stats.append('crossed once')
                elif match.teleop_rought == 3:
                    rought_stats.append('crossed twice')
                else:
                    rought_stats.append('not in play')
                if match.teleop_lowbar == 1:
                    lowbar_stats.append('got stuck')
                elif match.teleop_lowbar == 2:
                    lowbar_stats.append('crossed once')
                elif match.teleop_lowbar == 3:
                    lowbar_stats.append('crossed twice')
                else:
                    lowbar_stats.append('not in play')
                if match.teleop_ramparts == 1:
                    ramparts_stats.append('got stuck')
                elif match.teleop_ramparts == 2:
                    ramparts_stats.append('crossed once')
                elif match.teleop_ramparts == 3:
                    ramparts_stats.append('crossed twice')
                else:
                    ramparts_stats.append('not in play')
                if match.teleop_rockwall == 1:
                    rockwall_stats.append('got stuck')
                elif match.teleop_rockwall == 2:
                    rockwall_stats.append('crossed once')
                elif match.teleop_rockwall == 3:
                    rockwall_stats.append('crossed twice')
                else:
                    rockwall_stats.append('not in play')

                if match.hang_input == 1:
                    hang_input_values.append('attempted')
                elif match.hang_input == 2:
                    hang_input_values.append('successful hang')
                else:
                    hang_input_values.append('did not try')

                auton_low_values.append(match.auton_low_goals)
                auton_high_values.append(match.auton_high_goals)
                teleop_low_values.append(match.teleop_low_goals)
                teleop_high_values.append(match.teleop_high_goals)
                auton_def_reached_values.append(match.auton_def_reached)
                auton_def_crossed_values.append(match.auton_def_crossed)
                played_def_values.append(match.played_def)
                match_number.append(match.match_number)
            # team = get_object_or_404(Team, team_number=team_number)
            # team_number is the variable that will now allow you to do all the
            # things
            return render(request, 'team-raw-stats.html', {
                'teams': team,
                'hang_input_values': hang_input_values,
                'auton_low_values': auton_low_values,
                'auton_high_values': auton_high_values,
                'teleop_low_values': teleop_low_values,
                'teleop_high_values': teleop_high_values,
                'auton_def_reached_values': auton_def_reached_values,
                'auton_def_crossed_values': auton_def_crossed_values,
                'played_def_values': played_def_values,
                'portc_stats': portc_stats,
                'drawb_stats': drawb_stats,
                'cdf_stats': cdf_stats,
                'moat_stats': moat_stats,
                'sallyp_stats': sallyp_stats,
                'rought_stats': rought_stats,
                'lowbar_stats': lowbar_stats,
                'ramparts_stats': ramparts_stats,
                'rockwall_stats': rockwall_stats,
                'match_number': match_number

            })
        except:
            context = {}
            return render(request, 'no-team.html', context)
    else:
        context = {}
        return render(request, 'non-team.html', context)


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
