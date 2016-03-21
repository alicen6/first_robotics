from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from frcstats.models import Team, Match, Drive
from frcstats.forms import MatchForm, DriveForm
from django.views.generic import View
from django import forms
from frcstats.choices import auton_def_choices
from django.db import connection


def team_compare_info(request, first_team, second_team):
    team_one = Team.objects.filter(team_number=first_team)
    team_two = Team.objects.filter(team_number=second_team)

    def auto_lows(value):
        return sum(value) / float(len(value))

    def auto_highs(value):
        return sum(value) / float(len(value))

    def teleop_lows(value):
        return sum(value) / float(len(value))

    def teleop_highs(value):
        return sum(value) / float(len(value))

    def defense_cross(value, miss):
        if len(value) != 0 or len(miss) != 0:
            return (sum(value) - float(len(value))) / (float(len(value)) + float(len(miss)))
        else:
            return 0

    def defense_stuck(value, miss, stuck):
        if len(value) != 0 or len(miss) != 0:
            return str(int((float(len(stuck)) /
                            (float(len(value)) + float(len(miss)) + float(len(stuck)))) * 100)) + "%"
        else:
            return 0

    def played_def(value):
        return str(int((sum(value) / float(len(value))) * 100)) + "%"

    def hang_total(input, success, fail):
        return str(int((float(len(input)) + float(len(success))) / (float(len(input)) + float(len(success)) + float(len(fail))) * 100)) + "%"

    def hang_succes(input, success):
        return str(int(float(len(success)) / (float(len(success)) + float(len(input))) * 100)) + "%"

    def hang_fail(input, fail):
        if len(input) != 0 or len(fail) != 0:
            return str(int(float(len(fail)) / (float(len(fail)) + float(len(input))) * 100)) + "%"
        else:
            return "0%"

    if len(team_one) > 0 or len(team_two) > 0:
        team_one_matches = Match.objects.filter(team_number=team_one[0].id)
        team_two_matches = Match.objects.filter(team_number=team_two[0].id)
        team_one_drive = Drive.objects.filter(team_number=team_one[0].id)
        team_two_drive = Drive.objects.filter(team_number=team_two[0].id)
        drivetrain_one = []
        drivetrain_two = []
        gear_reduc_one = []
        gear_reduc_two = []
        motors_one = []
        motors_two = []
        notes_one = []
        notes_two = []
        auton_low_values_one = []
        auton_high_values_one = []
        auton_def_reached_values_one = []
        auton_def_crossed_values_one = []
        teleop_low_values_one = []
        teleop_high_values_one = []
        auton_low_values_two = []
        auton_high_values_two = []
        auton_def_reached_values_two = []
        auton_def_crossed_values_two = []
        teleop_low_values_two = []
        teleop_high_values_two = []
        hang_input_values_one = []
        hang_success_values_one = []
        hang_fail_values_one = []
        hang_input_values_two = []
        hang_success_values_two = []
        hang_fail_values_two = []
        played_def_values_one = []
        played_def_values_two = []
        portc_stats_one = []
        portc_stuck_stats_one = []
        drawb_stats_one = []
        drawb_stuck_stats_one = []
        cdf_stats_one = []
        cdf_stuck_stats_one = []
        moat_stats_one = []
        moat_stuck_stats_one = []
        sallyp_stats_one = []
        sallyp_stuck_stats_one = []
        rought_stats_one = []
        rought_stuck_stats_one = []
        lowbar_stats_one = []
        lowbar_stuck_stats_one = []
        ramparts_stats_one = []
        ramparts_stuck_stats_one = []
        rockwall_stats_one = []
        rockwall_stuck_stats_one = []
        portc_miss_stats_one = []
        drawb_miss_stats_one = []
        cdf_miss_stats_one = []
        moat_miss_stats_one = []
        sallyp_miss_stats_one = []
        rought_miss_stats_one = []
        lowbar_miss_stats_one = []
        ramparts_miss_stats_one = []
        rockwall_miss_stats_one = []
        portc_stats_two = []
        portc_stuck_stats_two = []
        drawb_stats_two = []
        drawb_stuck_stats_two = []
        cdf_stats_two = []
        cdf_stuck_stats_two = []
        moat_stats_two = []
        moat_stuck_stats_two = []
        sallyp_stats_two = []
        sallyp_stuck_stats_two = []
        rought_stats_two = []
        rought_stuck_stats_two = []
        lowbar_stats_two = []
        lowbar_stuck_stats_two = []
        ramparts_stats_two = []
        ramparts_stuck_stats_two = []
        rockwall_stats_two = []
        rockwall_stuck_stats_two = []
        portc_miss_stats_two = []
        drawb_miss_stats_two = []
        cdf_miss_stats_two = []
        moat_miss_stats_two = []
        sallyp_miss_stats_two = []
        rought_miss_stats_two = []
        lowbar_miss_stats_two = []
        ramparts_miss_stats_two = []
        rockwall_miss_stats_two = []
        for entry in team_one_drive:
            drivetrain_one.append(entry.drivetrain)
            gear_reduc_one.append(entry.gear_reduc)
            motors_one.append(entry.motors)
            notes_one.append(entry.extra_notes)
        for entry in team_two_drive:
            drivetrain_two.append(entry.drivetrain)
            gear_reduc_two.append(entry.gear_reduc)
            motors_two.append(entry.motors)
            notes_two.append(entry.extra_notes)
        for match in team_one_matches:
            auton_low_values_one.append(match.auton_low_goals)
            auton_high_values_one.append(match.auton_high_goals)
            teleop_low_values_one.append(match.teleop_low_goals)
            teleop_high_values_one.append(match.teleop_high_goals)
            auton_def_reached_values_one.append(match.auton_def_reached)
            auton_def_crossed_values_one.append(match.auton_def_crossed)
            played_def_values_one.append(match.played_def)
            if match.hang_input == 1:
                hang_input_values_one.append(match.hang_input)
            elif match.hang_input == 2:
                hang_success_values_one.append(match.hang_input)
            else:
                hang_fail_values_one.append(match.hang_input)
            if match.teleop_portc == 1:
                portc_stuck_stats_one.append(match.teleop_portc)
            elif match.teleop_portc == 4:
                portc_miss_stats_one.append(match.teleop_portc)
            elif match.teleop_portc != 0:
                portc_stats_one.append(match.teleop_portc)
            else:
                pass
            if match.teleop_drawb == 1:
                drawb_stuck_stats_one.append(match.teleop_drawb)
            elif match.teleop_drawb == 4:
                drawb_miss_stats_one.append(match.teleop_drawb)
            elif match.teleop_drawb != 0:
                drawb_stats_one.append(match.teleop_drawb)
            else:
                pass
            if match.teleop_cdf == 1:
                cdf_stuck_stats_one.append(match.teleop_cdf)
            elif match.teleop_cdf == 4:
                cdf_miss_stats_one.append(match.teleop_cdf)
            elif match.teleop_cdf != 0:
                cdf_stats_one.append(match.teleop_cdf)
            else:
                pass
            if match.teleop_moat == 1:
                moat_stuck_stats_one.append(match.teleop_moat)
            elif match.teleop_moat == 4:
                moat_miss_stats_one.append(match.teleop_moat)
            elif match.teleop_moat != 0:
                moat_stats_one.append(match.teleop_moat)
            else:
                pass
            if match.teleop_sallyp == 1:
                sallyp_stuck_stats_one.append(match.teleop_sallyp)
            elif match.teleop_sallyp == 4:
                sallyp_miss_stats_one.append(match.teleop_sallyp)
            elif match.teleop_sallyp != 0:
                sallyp_stats_one.append(match.teleop_sallyp)
            else:
                pass
            if match.teleop_rought == 1:
                rought_stuck_stats_one.append(match.teleop_rought)
            elif match.teleop_rought == 4:
                rought_miss_stats_one.append(match.teleop_rought)
            elif match.teleop_rought != 0:
                rought_stats_one.append(match.teleop_rought)
            else:
                pass
            if match.teleop_lowbar == 1:
                lowbar_stuck_stats_one.append(match.teleop_lowbar)
            elif match.teleop_lowbar == 4:
                lowbar_miss_stats_one.append(match.teleop_lowbar)
            elif match.teleop_lowbar != 0:
                lowbar_stats_one.append(match.teleop_lowbar)
            else:
                pass
            if match.teleop_ramparts == 1:
                ramparts_stuck_stats_one.append(match.teleop_ramparts)
            elif match.teleop_ramparts == 4:
                ramparts_miss_stats_one.append(match.teleop_ramparts)
            elif match.teleop_ramparts != 0:
                ramparts_stats_one.append(match.teleop_ramparts)
            else:
                pass
            if match.teleop_rockwall == 1:
                rockwall_stuck_stats_one.append(match.teleop_rockwall)
            elif match.teleop_rockwall == 4:
                rockwall_miss_stats_one.append(match.teleop_rockwall)
            elif match.teleop_rockwall != 0:
                rockwall_stats_one.append(match.teleop_rockwall)
            else:
                pass
        portc_stats_value_one = defense_cross(
            portc_stats_one, portc_miss_stats_one)
        portc_stuck_stats_one = defense_stuck(
            portc_stats_one, portc_miss_stats_one, portc_stuck_stats_one)
        drawb_stats_value_one = defense_cross(
            drawb_stats_one, drawb_miss_stats_one)
        drawb_stuck_stats_one = defense_stuck(
            drawb_stats_one, drawb_miss_stats_one, drawb_stuck_stats_one)
        cdf_stats_value_one = defense_cross(cdf_stats_one, cdf_miss_stats_one)
        cdf_stuck_stats_one = defense_stuck(
            cdf_stats_one, cdf_miss_stats_one, cdf_stuck_stats_one)
        moat_stats_value_one = defense_cross(
            moat_stats_one, moat_miss_stats_one)
        moat_stuck_stats_one = defense_stuck(
            moat_stats_one, moat_miss_stats_one, moat_stuck_stats_one)
        sallyp_stats_value_one = defense_cross(
            sallyp_stats_one, sallyp_miss_stats_one)
        sallyp_stuck_stats_one = defense_stuck(
            sallyp_stats_one, sallyp_miss_stats_one, sallyp_stuck_stats_one)
        rought_stats_value_one = defense_cross(
            rought_stats_one, rought_miss_stats_one)
        rought_stuck_stats_one = defense_stuck(
            rought_stats_one, rought_miss_stats_one, rought_stuck_stats_one)
        lowbar_stats_value_one = defense_cross(
            lowbar_stats_one, lowbar_miss_stats_one)
        lowbar_stuck_stats_one = defense_stuck(
            lowbar_stats_one, lowbar_miss_stats_one, lowbar_stuck_stats_one)
        ramparts_stats_value_one = defense_cross(
            ramparts_stats_one, ramparts_miss_stats_one)
        ramparts_stuck_stats_one = defense_stuck(
            ramparts_stats_one, ramparts_miss_stats_one, ramparts_stuck_stats_one)
        rockwall_stats_value_one = defense_cross(
            rockwall_stats_one, rockwall_miss_stats_one)
        rockwall_stuck_stats_one = defense_stuck(
            rockwall_stats_one, rockwall_miss_stats_one, rockwall_stuck_stats_one)
        hang_success_stats_one = hang_succes(
            hang_input_values_one, hang_success_values_one)
        played_def_stats_one = played_def(played_def_values_one)
        hang_value_one = hang_total(
            hang_input_values_one, hang_success_values_one, hang_fail_values_one)
        hang_fail_one = hang_fail(hang_input_values_one, hang_fail_values_one)
        auton_low_stats_one = auto_lows(auton_low_values_one)
        auton_high_stats_one = auto_highs(auton_high_values_one)
        teleop_low_stats_one = teleop_lows(teleop_low_values_one)
        teleop_high_stats_one = teleop_highs(teleop_high_values_one)

        for match in team_two_matches:
            auton_low_values_two.append(match.auton_low_goals)
            auton_high_values_two.append(match.auton_high_goals)
            teleop_low_values_two.append(match.teleop_low_goals)
            teleop_high_values_two.append(match.teleop_high_goals)
            auton_def_reached_values_two.append(match.auton_def_reached)
            auton_def_crossed_values_two.append(match.auton_def_crossed)
            played_def_values_two.append(match.played_def)
            if match.hang_input == 1:
                hang_input_values_two.append(match.hang_input)
            elif match.hang_input == 2:
                hang_success_values_two.append(match.hang_input)
            else:
                hang_fail_values_two.append(match.hang_input)
            if match.teleop_portc == 1:
                portc_stuck_stats_two.append(match.teleop_portc)
            elif match.teleop_portc == 4:
                portc_miss_stats_two.append(match.teleop_portc)
            elif match.teleop_portc != 0:
                portc_stats_two.append(match.teleop_portc)
            else:
                pass
            if match.teleop_drawb == 1:
                drawb_stuck_stats_two.append(match.teleop_drawb)
            elif match.teleop_drawb == 4:
                drawb_miss_stats_two.append(match.teleop_drawb)
            elif match.teleop_drawb != 0:
                drawb_stats_two.append(match.teleop_drawb)
            else:
                pass
            if match.teleop_cdf == 1:
                cdf_stuck_stats_two.append(match.teleop_cdf)
            elif match.teleop_cdf == 4:
                cdf_miss_stats_two.append(match.teleop_cdf)
            elif match.teleop_cdf != 0:
                cdf_stats_two.append(match.teleop_cdf)
            else:
                pass
            if match.teleop_moat == 1:
                moat_stuck_stats_two.append(match.teleop_moat)
            elif match.teleop_moat == 4:
                moat_miss_stats_two.append(match.teleop_moat)
            elif match.teleop_moat != 0:
                moat_stats_two.append(match.teleop_moat)
            else:
                pass
            if match.teleop_sallyp == 1:
                sallyp_stuck_stats_two.append(match.teleop_sallyp)
            elif match.teleop_sallyp == 4:
                sallyp_miss_stats_two.append(match.teleop_sallyp)
            elif match.teleop_sallyp != 0:
                sallyp_stats_two.append(match.teleop_sallyp)
            else:
                pass
            if match.teleop_rought == 1:
                rought_stuck_stats_two.append(match.teleop_rought)
            elif match.teleop_rought == 4:
                rought_miss_stats_two.append(match.teleop_rought)
            elif match.teleop_rought != 0:
                rought_stats_two.append(match.teleop_rought)
            else:
                pass
            if match.teleop_lowbar == 1:
                lowbar_stuck_stats_two.append(match.teleop_lowbar)
            elif match.teleop_lowbar == 4:
                lowbar_miss_stats_two.append(match.teleop_lowbar)
            elif match.teleop_lowbar != 0:
                lowbar_stats_two.append(match.teleop_lowbar)
            else:
                pass
            if match.teleop_ramparts == 1:
                ramparts_stuck_stats_two.append(match.teleop_ramparts)
            elif match.teleop_ramparts == 4:
                ramparts_miss_stats_two.append(match.teleop_ramparts)
            elif match.teleop_ramparts != 0:
                ramparts_stats_two.append(match.teleop_ramparts)
            else:
                pass
            if match.teleop_rockwall == 1:
                rockwall_stuck_stats_two.append(match.teleop_rockwall)
            elif match.teleop_rockwall == 4:
                rockwall_miss_stats_two.append(match.teleop_rockwall)
            elif match.teleop_rockwall != 0:
                rockwall_stats_two.append(match.teleop_rockwall)
            else:
                pass
            portc_stats_value_two = defense_cross(
                portc_stats_two, portc_miss_stats_two)
            portc_stuck_percent_two = defense_stuck(
                portc_stats_two, portc_miss_stats_two, portc_stuck_stats_two)
            drawb_stats_value_two = defense_cross(
                drawb_stats_two, drawb_miss_stats_two)
            drawb_stuck_percent_two = defense_stuck(
                drawb_stats_two, drawb_miss_stats_two, drawb_stuck_stats_two)
            cdf_stats_value_two = defense_cross(
                cdf_stats_two, cdf_miss_stats_two)
            cdf_stuck_percent_two = defense_stuck(
                cdf_stats_two, cdf_miss_stats_two, cdf_stuck_stats_two)
            moat_stats_value_two = defense_cross(
                moat_stats_two, moat_miss_stats_two)
            moat_stuck_percent_two = defense_stuck(
                moat_stats_two, moat_miss_stats_two, moat_stuck_stats_two)
            sallyp_stats_value_two = defense_cross(
                sallyp_stats_two, sallyp_miss_stats_two)
            sallyp_stuck_percent_two = defense_stuck(
                sallyp_stats_two, sallyp_miss_stats_two, sallyp_stuck_stats_two)
            rought_stats_value_two = defense_cross(
                rought_stats_two, rought_miss_stats_two)
            rought_stuck_percent_two = defense_stuck(
                rought_stats_two, rought_miss_stats_two, rought_stuck_stats_two)
            lowbar_stats_value_two = defense_cross(
                lowbar_stats_two, lowbar_miss_stats_two)
            lowbar_stuck_percent_two = defense_stuck(
                lowbar_stats_two, lowbar_miss_stats_two, lowbar_stuck_stats_two)
            ramparts_stats_value_two = defense_cross(
                ramparts_stats_two, ramparts_miss_stats_two)
            ramparts_stuck_percent_two = defense_stuck(
                ramparts_stats_two, ramparts_miss_stats_two, ramparts_stuck_stats_two)
            rockwall_stats_value_two = defense_cross(
                rockwall_stats_two, rockwall_miss_stats_two)
            rockwall_stuck_percent_two = defense_stuck(
                rockwall_stats_two, rockwall_miss_stats_two, rockwall_stuck_stats_two)
            hang_success_stats_two = hang_succes(
                hang_input_values_two, hang_success_values_two)
            played_def_stats_two = played_def(played_def_values_two)
            hang_value_two = hang_total(
                hang_input_values_two, hang_success_values_two, hang_fail_values_two)
            hang_fail_percent_two = hang_fail(
                hang_input_values_two, hang_fail_values_two)
            auton_low_stats_two = auto_lows(auton_low_values_two)
            auton_high_stats_two = auto_highs(auton_high_values_two)
            teleop_low_stats_two = teleop_lows(teleop_low_values_two)
            teleop_high_stats_two = teleop_highs(teleop_high_values_two)

        return render(request, 'team-compare.html', {
            'team_one': team_one,
            'portc_stats_value_one': portc_stats_value_one,
            'portc_stuck_stats_one': portc_stuck_stats_one,
            'drawb_stats_value_one': drawb_stats_value_one,
            'drawb_stuck_stats_one': drawb_stuck_stats_one,
            'cdf_stats_value_one': cdf_stats_value_one,
            'cdf_stuck_stats_one': cdf_stuck_stats_one,
            'moat_stats_value_one': moat_stats_value_one,
            'moat_stuck_stats_one': moat_stuck_stats_one,
            'sallyp_stats_value_one': sallyp_stats_value_one,
            'sallyp_stuck_stats_one': sallyp_stuck_stats_one,
            'rought_stats_value_one': rought_stats_value_one,
            'rought_stuck_stats_one': rought_stuck_stats_one,
            'lowbar_stats_value_one': lowbar_stats_value_one,
            'lowbar_stuck_stats_one': lowbar_stuck_stats_one,
            'ramparts_stats_value_one': ramparts_stats_value_one,
            'ramparts_stuck_stats_one': ramparts_stuck_stats_one,
            'rockwall_stats_value_one': rockwall_stats_value_one,
            'rockwall_stuck_stats_one': rockwall_stuck_stats_one,
            'drivetrain_one': drivetrain_one,
            'gear_reduc_one': gear_reduc_one,
            'motors_one': motors_one,
            'notes_one': notes_one,
            'hang_success_stats_one': hang_success_stats_one,
            'played_def_stats_one': played_def_stats_one,
            'hang_value_one': hang_value_one,
            'hang_fail_one': hang_fail_one,
            'auton_low_stats_one': auton_low_stats_one,
            'auton_high_stats_one': auton_high_stats_one,
            'teleop_low_stats_one': teleop_low_stats_one,
            'teleop_high_stats_one': teleop_high_stats_one,
            'auton_def_reached_values_one': list({auton_def_choices[x] for x in auton_def_reached_values_one}),
            'auton_def_crossed_values_one': list({auton_def_choices[x] for x in auton_def_crossed_values_one}),
            'team_two': team_two,
            'hang_value_two': hang_value_two,
            'hang_fail_percent_two': hang_fail_percent_two,
            'auton_low_stats_two': auton_low_stats_two,
            'auton_high_stats_two': auton_high_stats_two,
            'teleop_low_stats_two': teleop_low_stats_two,
            'teleop_high_stats_two': teleop_high_stats_two,
            'auton_def_reached_values_two': list({auton_def_choices[x] for x in auton_def_reached_values_two}),
            'auton_def_crossed_values_two': list({auton_def_choices[x] for x in auton_def_crossed_values_two}),
            'played_def_stats_two': played_def_stats_two,
            'portc_stats_value_two': portc_stats_value_two,
            'portc_stuck_percent_two': portc_stuck_percent_two,
            'drawb_stats_value_two': drawb_stats_value_two,
            'drawb_stuck_percent_two': drawb_stuck_percent_two,
            'cdf_stats_value_two': cdf_stats_value_two,
            'cdf_stuck_percent_two': cdf_stuck_percent_two,
            'moat_stats_value_two': moat_stats_value_two,
            'moat_stuck_percent_two': moat_stuck_percent_two,
            'sallyp_stats_value_two': sallyp_stats_value_two,
            'sallyp_stuck_percent_two': sallyp_stuck_percent_two,
            'rought_stats_value_two': rought_stats_value_two,
            'rought_stuck_percent_two': rought_stuck_percent_two,
            'lowbar_stats_value_two': lowbar_stats_value_two,
            'lowbar_stuck_percent_two': lowbar_stuck_percent_two,
            'ramparts_stats_value_two': ramparts_stats_value_two,
            'ramparts_stuck_percent_two': ramparts_stuck_percent_two,
            'rockwall_stats_value_two': rockwall_stats_value_two,
            'rockwall_stuck_percent_two': rockwall_stuck_percent_two,
            'hang_success_stats_two': hang_success_stats_two,
            'drivetrain_two': drivetrain_two,
            'gear_reduc_two': gear_reduc_two,
            'motors_two': motors_two,
            'notes_two': notes_two
        })
