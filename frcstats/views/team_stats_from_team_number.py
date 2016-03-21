from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.forms import ModelForm, modelform_factory
from frcstats.models import Team, Match, Drive
from django.views.generic import View
from django import forms
from django.db import connection


def team_stats_from_team_number(request, team_number):
    def divide(values, nope):
        if len(values) != 0 or len(nope) != 0:
            return (sum(values) - float(len(values))) / (float(len(values)) + float(len(nope))) \
                # if len(values) != 0 else 0
        else:
            return 0

    def stuck_divide(values, stuck, nope):
        if len(values) != 0 or len(nope) != 0:
            return str(int(float(len(stuck)) /
                           (float(len(values)) + float(len(nope)) + float(len(stuck)))) * 100) + "%"
        else:
            return 0
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
        portc_miss_stats = []
        drawb_miss_stats = []
        cdf_miss_stats = []
        moat_miss_stats = []
        sallyp_miss_stats = []
        rought_miss_stats = []
        lowbar_miss_stats = []
        ramparts_miss_stats = []
        rockwall_miss_stats = []
        try:
            for match in matches:
                if match.teleop_portc == 1:
                    portc_stuck_stats.append(match.teleop_portc)
                elif match.teleop_portc == 4:
                    portc_miss_stats.append(match.teleop_portc)
                elif match.teleop_portc != 0:
                    portc_stats.append(match.teleop_portc)
                else:
                    pass
                if match.teleop_drawb == 1:
                    drawb_stuck_stats.append(match.teleop_drawb)
                elif match.teleop_drawb == 4:
                    drawb_miss_stats.append(match.teleop_drawb)
                elif match.teleop_drawb != 0:
                    drawb_stats.append(match.teleop_drawb)
                else:
                    pass
                if match.teleop_cdf == 1:
                    cdf_stuck_stats.append(match.teleop_cdf)
                elif match.teleop_cdf == 4:
                    cdf_miss_stats.append(match.teleop_cdf)
                elif match.teleop_cdf != 0:
                    cdf_stats.append(match.teleop_cdf)
                else:
                    pass
                if match.teleop_moat == 1:
                    moat_stuck_stats.append(match.teleop_moat)
                elif match.teleop_moat == 4:
                    moat_miss_stats.append(match.teleop_moat)
                elif match.teleop_moat != 0:
                    moat_stats.append(match.teleop_moat)
                else:
                    pass
                if match.teleop_sallyp == 1:
                    sallyp_stuck_stats.append(match.teleop_sallyp)
                elif match.teleop_sallyp == 4:
                    sallyp_miss_stats.append(match.teleop_sallyp)
                elif match.teleop_sallyp != 0:
                    sallyp_stats.append(match.teleop_sallyp)
                else:
                    pass
                if match.teleop_rought == 1:
                    rought_stuck_stats.append(match.teleop_rought)
                elif match.teleop_rought == 4:
                    rought_miss_stats.append(match.teleop_rought)
                elif match.teleop_rought != 0:
                    rought_stats.append(match.teleop_rought)
                else:
                    pass
                if match.teleop_lowbar == 1:
                    lowbar_stuck_stats.append(match.teleop_lowbar)
                elif match.teleop_lowbar == 4:
                    lowbar_miss_stats.append(match.teleop_lowbar)
                elif match.teleop_lowbar != 0:
                    lowbar_stats.append(match.teleop_lowbar)
                else:
                    pass
                if match.teleop_ramparts == 1:
                    ramparts_stuck_stats.append(match.teleop_ramparts)
                elif match.teleop_ramparts == 4:
                    ramparts_miss_stats.append(match.teleop_ramparts)
                elif match.teleop_ramparts != 0:
                    ramparts_stats.append(match.teleop_ramparts)
                else:
                    pass
                if match.teleop_rockwall == 1:
                    rockwall_stuck_stats.append(match.teleop_rockwall)
                elif match.teleop_rockwall == 4:
                    rockwall_miss_stats.append(match.teleop_rockwall)
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
            portc_stats_value = divide(portc_stats, portc_miss_stats)
            portc_stuck_stats = stuck_divide(
                portc_stats, portc_stuck_stats, portc_miss_stats)
            drawb_stats_value = divide(drawb_stats, drawb_miss_stats)
            drawb_stuck_stats = stuck_divide(
                drawb_stats, drawb_stuck_stats, drawb_miss_stats)
            cdf_stats_value = divide(cdf_stats, cdf_miss_stats)
            cdf_stuck_stats = stuck_divide(
                cdf_stats, cdf_stuck_stats, cdf_miss_stats)
            moat_stats_value = divide(moat_stats, moat_miss_stats)
            moat_stuck_stats = stuck_divide(
                moat_stats, moat_stuck_stats, moat_miss_stats)
            sallyp_stats_value = divide(sallyp_stats, sallyp_miss_stats)
            sallyp_stuck_stats = stuck_divide(
                sallyp_stats, sallyp_stuck_stats, sallyp_miss_stats)
            rought_stats_value = divide(rought_stats, rought_miss_stats)
            rought_stuck_stats = stuck_divide(
                rought_stats, rought_stuck_stats, rought_miss_stats)
            lowbar_stats_value = divide(lowbar_stats, lowbar_miss_stats)
            lowbar_stuck_stats = stuck_divide(
                lowbar_stats, lowbar_stuck_stats, lowbar_miss_stats)
            ramparts_stats_value = divide(ramparts_stats, ramparts_miss_stats)
            ramparts_stuck_stats = stuck_divide(
                ramparts_stats, ramparts_stuck_stats, ramparts_miss_stats)
            rockwall_stats_value = divide(rockwall_stats, rockwall_miss_stats)
            rockwall_stuck_stats = stuck_divide(
                rockwall_stats, rockwall_stuck_stats, rockwall_miss_stats)
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
