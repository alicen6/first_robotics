from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from frcstats.models import Team
from django.views.generic import View
from django import forms
from django.db import connection


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
                elif match.teleop_portc == 4:
                    portc_stats.append('did not cross')
                else:
                    portc_stats.append('not in play')
                if match.teleop_drawb == 1:
                    drawb_stats.append('got stuck')
                elif match.teleop_drawb == 2:
                    drawb_stats.append('crossed once')
                elif match.teleop_drawb == 3:
                    drawb_stats.append('crossed twice')
                elif match.teleop_drawb == 4:
                    drawb_stats.append('did not cross')
                else:
                    drawb_stats.append('not in play')
                if match.teleop_cdf == 1:
                    cdf_stats.append('got stuck')
                elif match.teleop_cdf == 2:
                    cdf_stats.append('crossed once')
                elif match.teleop_cdf == 3:
                    cdf_stats.append('crossed twice')
                elif match.teleop_cdf == 4:
                    cdf_stats.append('did not cross')
                else:
                    cdf_stats.append('not in play')
                if match.teleop_moat == 1:
                    moat_stats.append('got stuck')
                elif match.teleop_moat == 2:
                    moat_stats.append('crossed once')
                elif match.teleop_moat == 3:
                    moat_stats.append('crossed twice')
                elif match.teleop_moat == 4:
                    moat_stats.append('did not cross')
                else:
                    moat_stats.append('not in play')
                if match.teleop_sallyp == 1:
                    sallyp_stats.append('got stuck')
                elif match.teleop_sallyp == 2:
                    sallyp_stats.append('crossed once')
                elif match.teleop_sallyp == 3:
                    sallyp_stats.append('crossed twice')
                elif match.teleop_sallyp == 4:
                    sallyp_stats.append('did not cross')
                else:
                    sallyp_stats.append('not in play')
                if match.teleop_rought == 1:
                    rought_stats.append('got stuck')
                elif match.teleop_rought == 2:
                    rought_stats.append('crossed once')
                elif match.teleop_rought == 3:
                    rought_stats.append('crossed twice')
                elif match.teleop_rought == 4:
                    rought_stats.append('did not cross')
                else:
                    rought_stats.append('not in play')
                if match.teleop_lowbar == 1:
                    lowbar_stats.append('got stuck')
                elif match.teleop_lowbar == 2:
                    lowbar_stats.append('crossed once')
                elif match.teleop_lowbar == 3:
                    lowbar_stats.append('crossed twice')
                elif match.teleop_lowbar == 4:
                    lowbar_stats.append('did not cross')
                else:
                    lowbar_stats.append('not in play')
                if match.teleop_ramparts == 1:
                    ramparts_stats.append('got stuck')
                elif match.teleop_ramparts == 2:
                    ramparts_stats.append('crossed once')
                elif match.teleop_ramparts == 3:
                    ramparts_stats.append('crossed twice')
                elif match.teleop_ramparts == 4:
                    ramparts_stats.append('did not cross')
                else:
                    ramparts_stats.append('not in play')
                if match.teleop_rockwall == 1:
                    rockwall_stats.append('got stuck')
                elif match.teleop_rockwall == 2:
                    rockwall_stats.append('crossed once')
                elif match.teleop_rockwall == 3:
                    rockwall_stats.append('crossed twice')
                elif match.teleop_rockwall == 4:
                    rockwall_stats.append('did not cross')
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
