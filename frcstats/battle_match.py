from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.forms import ModelForm, modelform_factory
from .models import Team, Match
import random


def battle_match(request, red_one, red_two, red_three, blue_one, blue_two, blue_three):
    red_one_number = red_one
    red_number_two = red_two
    red_number_three = red_three
    blue_number_one = blue_one
    blue_number_two = blue_two
    blue_number_three = blue_three

    red_one = Team.objects.filter(team_number=red_one)
    red_two = Team.objects.filter(team_number=red_two)
    red_three = Team.objects.filter(team_number=red_three)

    blue_one = Team.objects.filter(team_number=blue_one)
    blue_two = Team.objects.filter(team_number=blue_two)
    blue_three = Team.objects.filter(team_number=blue_three)

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
            return float(len(stuck)) / \
                (float(len(value)) + float(len(miss)) + float(len(stuck)))
        else:
            return 0

    def played_def(value):
        return sum(value) / float(len(value))

    def hang_total(input, success, fail):
        if len(input) != 0 or len(success) != 0 or len(fail) != 0:
            return (float(len(input)) + float(len(success))) / (float(len(input)) + float(len(success)) + float(len(fail)))
        else:
            return 0

    def hang_succes(input, success):
        if len(input) != 0 or len(success) != 0:
            return float(len(success)) / (float(len(success)) + float(len(input)))
        else:
            return 0

    def hang_fail(input, fail):
        if len(input) != 0 or len(fail) != 0:
            return float(len(fail)) / (float(len(fail)) + float(len(input)))
        else:
            return 0

    if len(red_one) > 0 or len(blue_one) > 0:
        red_one_matches = Match.objects.filter(team_number=red_one[0].id)
        red_two_matches = Match.objects.filter(team_number=red_two[0].id)
        red_three_matches = Match.objects.filter(team_number=red_three[0].id)
        blue_one_matches = Match.objects.filter(team_number=blue_one[0].id)
        blue_two_matches = Match.objects.filter(team_number=blue_two[0].id)
        blue_three_matches = Match.objects.filter(team_number=blue_three[0].id)

        red_one_auton_low_values = []
        red_one_auton_high_values = []
        red_one_auton_def_reached_values = []
        red_one_auton_def_crossed_values = []
        red_one_teleop_low_values = []
        red_one_teleop_high_values = []
        red_one_hang_input_values = []
        red_one_hang_success_values = []
        red_one_hang_fail_values = []
        red_one_played_def_values = []
        red_one_portc_stats = []
        red_one_portc_stuck_stats = []
        red_one_drawb_stats = []
        red_one_drawb_stuck_stats = []
        red_one_cdf_stats = []
        red_one_cdf_stuck_stats = []
        red_one_moat_stats = []
        red_one_moat_stuck_stats = []
        red_one_sallyp_stats = []
        red_one_sallyp_stuck_stats = []
        red_one_rought_stats = []
        red_one_rought_stuck_stats = []
        red_one_lowbar_stats = []
        red_one_lowbar_stuck_stats = []
        red_one_ramparts_stats = []
        red_one_ramparts_stuck_stats = []
        red_one_rockwall_stats = []
        red_one_rockwall_stuck_stats = []
        red_one_portc_miss_stats = []
        red_one_drawb_miss_stats = []
        red_one_cdf_miss_stats = []
        red_one_moat_miss_stats = []
        red_one_sallyp_miss_stats = []
        red_one_rought_miss_stats = []
        red_one_lowbar_miss_stats = []
        red_one_ramparts_miss_stats = []
        red_one_rockwall_miss_stats = []

        red_two_auton_low_values = []
        red_two_auton_high_values = []
        red_two_auton_def_reached_values = []
        red_two_auton_def_crossed_values = []
        red_two_teleop_low_values = []
        red_two_teleop_high_values = []
        red_two_hang_input_values = []
        red_two_hang_success_values = []
        red_two_hang_fail_values = []
        red_two_played_def_values = []
        red_two_portc_stats = []
        red_two_portc_stuck_stats = []
        red_two_drawb_stats = []
        red_two_drawb_stuck_stats = []
        red_two_cdf_stats = []
        red_two_cdf_stuck_stats = []
        red_two_moat_stats = []
        red_two_moat_stuck_stats = []
        red_two_sallyp_stats = []
        red_two_sallyp_stuck_stats = []
        red_two_rought_stats = []
        red_two_rought_stuck_stats = []
        red_two_lowbar_stats = []
        red_two_lowbar_stuck_stats = []
        red_two_ramparts_stats = []
        red_two_ramparts_stuck_stats = []
        red_two_rockwall_stats = []
        red_two_rockwall_stuck_stats = []
        red_two_portc_miss_stats = []
        red_two_drawb_miss_stats = []
        red_two_cdf_miss_stats = []
        red_two_moat_miss_stats = []
        red_two_sallyp_miss_stats = []
        red_two_rought_miss_stats = []
        red_two_lowbar_miss_stats = []
        red_two_ramparts_miss_stats = []
        red_two_rockwall_miss_stats = []

        red_three_auton_low_values = []
        red_three_auton_high_values = []
        red_three_auton_def_reached_values = []
        red_three_auton_def_crossed_values = []
        red_three_teleop_low_values = []
        red_three_teleop_high_values = []
        red_three_hang_input_values = []
        red_three_hang_success_values = []
        red_three_hang_fail_values = []
        red_three_played_def_values = []
        red_three_portc_stats = []
        red_three_portc_stuck_stats = []
        red_three_drawb_stats = []
        red_three_drawb_stuck_stats = []
        red_three_cdf_stats = []
        red_three_cdf_stuck_stats = []
        red_three_moat_stats = []
        red_three_moat_stuck_stats = []
        red_three_sallyp_stats = []
        red_three_sallyp_stuck_stats = []
        red_three_rought_stats = []
        red_three_rought_stuck_stats = []
        red_three_lowbar_stats = []
        red_three_lowbar_stuck_stats = []
        red_three_ramparts_stats = []
        red_three_ramparts_stuck_stats = []
        red_three_rockwall_stats = []
        red_three_rockwall_stuck_stats = []
        red_three_portc_miss_stats = []
        red_three_drawb_miss_stats = []
        red_three_cdf_miss_stats = []
        red_three_moat_miss_stats = []
        red_three_sallyp_miss_stats = []
        red_three_rought_miss_stats = []
        red_three_lowbar_miss_stats = []
        red_three_ramparts_miss_stats = []
        red_three_rockwall_miss_stats = []

        blue_one_auton_low_values = []
        blue_one_auton_high_values = []
        blue_one_auton_def_reached_values = []
        blue_one_auton_def_crossed_values = []
        blue_one_teleop_low_values = []
        blue_one_teleop_high_values = []
        blue_one_hang_input_values = []
        blue_one_hang_success_values = []
        blue_one_hang_fail_values = []
        blue_one_played_def_values = []
        blue_one_portc_stats = []
        blue_one_portc_stuck_stats = []
        blue_one_drawb_stats = []
        blue_one_drawb_stuck_stats = []
        blue_one_cdf_stats = []
        blue_one_cdf_stuck_stats = []
        blue_one_moat_stats = []
        blue_one_moat_stuck_stats = []
        blue_one_sallyp_stats = []
        blue_one_sallyp_stuck_stats = []
        blue_one_rought_stats = []
        blue_one_rought_stuck_stats = []
        blue_one_lowbar_stats = []
        blue_one_lowbar_stuck_stats = []
        blue_one_ramparts_stats = []
        blue_one_ramparts_stuck_stats = []
        blue_one_rockwall_stats = []
        blue_one_rockwall_stuck_stats = []
        blue_one_portc_miss_stats = []
        blue_one_drawb_miss_stats = []
        blue_one_cdf_miss_stats = []
        blue_one_moat_miss_stats = []
        blue_one_sallyp_miss_stats = []
        blue_one_rought_miss_stats = []
        blue_one_lowbar_miss_stats = []
        blue_one_ramparts_miss_stats = []
        blue_one_rockwall_miss_stats = []

        blue_two_auton_low_values = []
        blue_two_auton_high_values = []
        blue_two_auton_def_reached_values = []
        blue_two_auton_def_crossed_values = []
        blue_two_teleop_low_values = []
        blue_two_teleop_high_values = []
        blue_two_hang_input_values = []
        blue_two_hang_success_values = []
        blue_two_hang_fail_values = []
        blue_two_played_def_values = []
        blue_two_portc_stats = []
        blue_two_portc_stuck_stats = []
        blue_two_drawb_stats = []
        blue_two_drawb_stuck_stats = []
        blue_two_cdf_stats = []
        blue_two_cdf_stuck_stats = []
        blue_two_moat_stats = []
        blue_two_moat_stuck_stats = []
        blue_two_sallyp_stats = []
        blue_two_sallyp_stuck_stats = []
        blue_two_rought_stats = []
        blue_two_rought_stuck_stats = []
        blue_two_lowbar_stats = []
        blue_two_lowbar_stuck_stats = []
        blue_two_ramparts_stats = []
        blue_two_ramparts_stuck_stats = []
        blue_two_rockwall_stats = []
        blue_two_rockwall_stuck_stats = []
        blue_two_portc_miss_stats = []
        blue_two_drawb_miss_stats = []
        blue_two_cdf_miss_stats = []
        blue_two_moat_miss_stats = []
        blue_two_sallyp_miss_stats = []
        blue_two_rought_miss_stats = []
        blue_two_lowbar_miss_stats = []
        blue_two_ramparts_miss_stats = []
        blue_two_rockwall_miss_stats = []

        blue_three_auton_low_values = []
        blue_three_auton_high_values = []
        blue_three_auton_def_reached_values = []
        blue_three_auton_def_crossed_values = []
        blue_three_teleop_low_values = []
        blue_three_teleop_high_values = []
        blue_three_hang_input_values = []
        blue_three_hang_success_values = []
        blue_three_hang_fail_values = []
        blue_three_played_def_values = []
        blue_three_portc_stats = []
        blue_three_portc_stuck_stats = []
        blue_three_drawb_stats = []
        blue_three_drawb_stuck_stats = []
        blue_three_cdf_stats = []
        blue_three_cdf_stuck_stats = []
        blue_three_moat_stats = []
        blue_three_moat_stuck_stats = []
        blue_three_sallyp_stats = []
        blue_three_sallyp_stuck_stats = []
        blue_three_rought_stats = []
        blue_three_rought_stuck_stats = []
        blue_three_lowbar_stats = []
        blue_three_lowbar_stuck_stats = []
        blue_three_ramparts_stats = []
        blue_three_ramparts_stuck_stats = []
        blue_three_rockwall_stats = []
        blue_three_rockwall_stuck_stats = []
        blue_three_portc_miss_stats = []
        blue_three_drawb_miss_stats = []
        blue_three_cdf_miss_stats = []
        blue_three_moat_miss_stats = []
        blue_three_sallyp_miss_stats = []
        blue_three_rought_miss_stats = []
        blue_three_lowbar_miss_stats = []
        blue_three_ramparts_miss_stats = []
        blue_three_rockwall_miss_stats = []

    for match in red_one_matches:
        red_one_auton_low_values.append(match.auton_low_goals)
        red_one_auton_high_values.append(match.auton_high_goals)
        red_one_teleop_low_values.append(match.teleop_low_goals)
        red_one_teleop_high_values.append(match.teleop_high_goals)
        red_one_auton_def_reached_values.append(match.auton_def_reached)
        red_one_auton_def_crossed_values.append(match.auton_def_crossed)
        red_one_played_def_values.append(match.played_def)
        if match.hang_input == 1:
            red_one_hang_input_values.append(match.hang_input)
        elif match.hang_input == 2:
            red_one_hang_success_values.append(match.hang_input)
        else:
            red_one_hang_fail_values.append(match.hang_input)
        if match.teleop_portc == 1:
            red_one_portc_stuck_stats.append(match.teleop_portc)
        elif match.teleop_portc == 4:
            red_one_portc_miss_stats.append(match.teleop_portc)
        elif match.teleop_portc != 0:
            red_one_portc_stats.append(match.teleop_portc)
        else:
            pass
        if match.teleop_drawb == 1:
            red_one_drawb_stuck_stats.append(match.teleop_drawb)
        elif match.teleop_drawb == 4:
            red_one_drawb_miss_stats.append(match.teleop_drawb)
        elif match.teleop_drawb != 0:
            red_one_drawb_stats.append(match.teleop_drawb)
        else:
            pass
        if match.teleop_cdf == 1:
            red_one_cdf_stuck_stats.append(match.teleop_cdf)
        elif match.teleop_cdf == 4:
            red_one_cdf_miss_stats.append(match.teleop_cdf)
        elif match.teleop_cdf != 0:
            red_one_cdf_stats.append(match.teleop_cdf)
        else:
            pass
        if match.teleop_moat == 1:
            red_one_moat_stuck_stats.append(match.teleop_moat)
        elif match.teleop_moat == 4:
            red_one_moat_miss_stats.append(match.teleop_moat)
        elif match.teleop_moat != 0:
            red_one_moat_stats.append(match.teleop_moat)
        else:
            pass
        if match.teleop_sallyp == 1:
            red_one_sallyp_stuck_stats.append(match.teleop_sallyp)
        elif match.teleop_sallyp == 4:
            red_one_sallyp_miss_stats.append(match.teleop_sallyp)
        elif match.teleop_sallyp != 0:
            red_one_sallyp_stats.append(match.teleop_sallyp)
        else:
            pass
        if match.teleop_rought == 1:
            red_one_rought_stuck_stats.append(match.teleop_rought)
        elif match.teleop_rought == 4:
            red_one_rought_miss_stats.append(match.teleop_rought)
        elif match.teleop_rought != 0:
            red_one_rought_stats.append(match.teleop_rought)
        else:
            pass
        if match.teleop_lowbar == 1:
            red_one_lowbar_stuck_stats.append(match.teleop_lowbar)
        elif match.teleop_lowbar == 4:
            red_one_lowbar_miss_stats.append(match.teleop_lowbar)
        elif match.teleop_lowbar != 0:
            red_one_lowbar_stats.append(match.teleop_lowbar)
        else:
            pass
        if match.teleop_ramparts == 1:
            red_one_ramparts_stuck_stats.append(match.teleop_ramparts)
        elif match.teleop_ramparts == 4:
            red_one_ramparts_miss_stats.append(match.teleop_ramparts)
        elif match.teleop_ramparts != 0:
            red_one_ramparts_stats.append(match.teleop_ramparts)
        else:
            pass
        if match.teleop_rockwall == 1:
            red_one_rockwall_stuck_stats.append(match.teleop_rockwall)
        elif match.teleop_rockwall == 4:
            red_one_rockwall_miss_stats.append(match.teleop_rockwall)
        elif match.teleop_rockwall != 0:
            red_one_rockwall_stats.append(match.teleop_rockwall)
        else:
            pass
    red_one_portc_stats_value = defense_cross(
        red_one_portc_stats, red_one_portc_miss_stats)
    red_one_portc_stuck_stats = defense_stuck(
        red_one_portc_stats, red_one_portc_miss_stats, red_one_portc_stuck_stats)
    red_one_drawb_stats_value = defense_cross(
        red_one_drawb_stats, red_one_drawb_miss_stats)
    red_one_drawb_stuck_stats = defense_stuck(
        red_one_drawb_stats, red_one_drawb_miss_stats, red_one_drawb_stuck_stats)
    red_one_cdf_stats_value = defense_cross(
        red_one_cdf_stats, red_one_cdf_miss_stats)
    red_one_cdf_stuck_stats = defense_stuck(
        red_one_cdf_stats, red_one_cdf_miss_stats, red_one_cdf_stuck_stats)
    red_one_moat_stats_value = defense_cross(
        red_one_moat_stats, red_one_moat_miss_stats)
    red_one_moat_stuck_stats = defense_stuck(
        red_one_moat_stats, red_one_moat_miss_stats, red_one_moat_stuck_stats)
    red_one_sallyp_stats_value = defense_cross(
        red_one_sallyp_stats, red_one_sallyp_miss_stats)
    red_one_sallyp_stuck_stats = defense_stuck(
        red_one_sallyp_stats, red_one_sallyp_miss_stats, red_one_sallyp_stuck_stats)
    red_one_rought_stats_value = defense_cross(
        red_one_rought_stats, red_one_rought_miss_stats)
    red_one_rought_stuck_stats = defense_stuck(
        red_one_rought_stats, red_one_rought_miss_stats, red_one_rought_stuck_stats)
    red_one_lowbar_stats_value = defense_cross(
        red_one_lowbar_stats, red_one_lowbar_miss_stats)
    red_one_lowbar_stuck_stats = defense_stuck(
        red_one_lowbar_stats, red_one_lowbar_miss_stats, red_one_lowbar_stuck_stats)
    red_one_ramparts_stats_value = defense_cross(
        red_one_ramparts_stats, red_one_ramparts_miss_stats)
    red_one_ramparts_stuck_stats = defense_stuck(
        red_one_ramparts_stats, red_one_ramparts_miss_stats, red_one_ramparts_stuck_stats)
    red_one_rockwall_stats_value = defense_cross(
        red_one_rockwall_stats, red_one_rockwall_miss_stats)
    red_one_rockwall_stuck_stats = defense_stuck(
        red_one_rockwall_stats, red_one_rockwall_miss_stats, red_one_rockwall_stuck_stats)
    red_one_hang_success_stats = hang_succes(
        red_one_hang_input_values, red_one_hang_success_values)
    red_one_played_def_stats = played_def(red_one_played_def_values)
    red_one_hang_value = hang_total(
        red_one_hang_input_values, red_one_hang_success_values, red_one_hang_fail_values)
    red_one_hang_fail = hang_fail(
        red_one_hang_input_values, red_one_hang_fail_values)
    red_one_auton_low_stats = auto_lows(red_one_auton_low_values)
    red_one_auton_high_stats = auto_highs(red_one_auton_high_values)
    red_one_teleop_low_stats = teleop_lows(red_one_teleop_low_values)
    red_one_teleop_high_stats = teleop_highs(red_one_teleop_high_values)

    for match in red_two_matches:
        red_two_auton_low_values.append(match.auton_low_goals)
        red_two_auton_high_values.append(match.auton_high_goals)
        red_two_teleop_low_values.append(match.teleop_low_goals)
        red_two_teleop_high_values.append(match.teleop_high_goals)
        red_two_auton_def_reached_values.append(match.auton_def_reached)
        red_two_auton_def_crossed_values.append(match.auton_def_crossed)
        red_two_played_def_values.append(match.played_def)
        if match.hang_input == 1:
            red_two_hang_input_values.append(match.hang_input)
        elif match.hang_input == 2:
            red_two_hang_success_values.append(match.hang_input)
        else:
            red_two_hang_fail_values.append(match.hang_input)
        if match.teleop_portc == 1:
            red_two_portc_stuck_stats.append(match.teleop_portc)
        elif match.teleop_portc == 4:
            red_two_portc_miss_stats.append(match.teleop_portc)
        elif match.teleop_portc != 0:
            red_two_portc_stats.append(match.teleop_portc)
        else:
            pass
        if match.teleop_drawb == 1:
            red_two_drawb_stuck_stats.append(match.teleop_drawb)
        elif match.teleop_drawb == 4:
            red_two_drawb_miss_stats.append(match.teleop_drawb)
        elif match.teleop_drawb != 0:
            red_two_drawb_stats.append(match.teleop_drawb)
        else:
            pass
        if match.teleop_cdf == 1:
            red_two_cdf_stuck_stats.append(match.teleop_cdf)
        elif match.teleop_cdf == 4:
            red_two_cdf_miss_stats.append(match.teleop_cdf)
        elif match.teleop_cdf != 0:
            red_two_cdf_stats.append(match.teleop_cdf)
        else:
            pass
        if match.teleop_moat == 1:
            red_two_moat_stuck_stats.append(match.teleop_moat)
        elif match.teleop_moat == 4:
            red_two_moat_miss_stats.append(match.teleop_moat)
        elif match.teleop_moat != 0:
            red_two_moat_stats.append(match.teleop_moat)
        else:
            pass
        if match.teleop_sallyp == 1:
            red_two_sallyp_stuck_stats.append(match.teleop_sallyp)
        elif match.teleop_sallyp == 4:
            red_two_sallyp_miss_stats.append(match.teleop_sallyp)
        elif match.teleop_sallyp != 0:
            red_two_sallyp_stats.append(match.teleop_sallyp)
        else:
            pass
        if match.teleop_rought == 1:
            red_two_rought_stuck_stats.append(match.teleop_rought)
        elif match.teleop_rought == 4:
            red_two_rought_miss_stats.append(match.teleop_rought)
        elif match.teleop_rought != 0:
            red_two_rought_stats.append(match.teleop_rought)
        else:
            pass
        if match.teleop_lowbar == 1:
            red_two_lowbar_stuck_stats.append(match.teleop_lowbar)
        elif match.teleop_lowbar == 4:
            red_two_lowbar_miss_stats.append(match.teleop_lowbar)
        elif match.teleop_lowbar != 0:
            red_two_lowbar_stats.append(match.teleop_lowbar)
        else:
            pass
        if match.teleop_ramparts == 1:
            red_two_ramparts_stuck_stats.append(match.teleop_ramparts)
        elif match.teleop_ramparts == 4:
            red_two_ramparts_miss_stats.append(match.teleop_ramparts)
        elif match.teleop_ramparts != 0:
            red_two_ramparts_stats.append(match.teleop_ramparts)
        else:
            pass
        if match.teleop_rockwall == 1:
            red_two_rockwall_stuck_stats.append(match.teleop_rockwall)
        elif match.teleop_rockwall == 4:
            red_two_rockwall_miss_stats.append(match.teleop_rockwall)
        elif match.teleop_rockwall != 0:
            red_two_rockwall_stats.append(match.teleop_rockwall)
        else:
            pass
    red_two_portc_stats_value = defense_cross(
        red_two_portc_stats, red_two_portc_miss_stats)
    red_two_portc_stuck_stats = defense_stuck(
        red_two_portc_stats, red_two_portc_miss_stats, red_two_portc_stuck_stats)
    red_two_drawb_stats_value = defense_cross(
        red_two_drawb_stats, red_two_drawb_miss_stats)
    red_two_drawb_stuck_stats = defense_stuck(
        red_two_drawb_stats, red_two_drawb_miss_stats, red_two_drawb_stuck_stats)
    red_two_cdf_stats_value = defense_cross(
        red_two_cdf_stats, red_two_cdf_miss_stats)
    red_two_cdf_stuck_stats = defense_stuck(
        red_two_cdf_stats, red_two_cdf_miss_stats, red_two_cdf_stuck_stats)
    red_two_moat_stats_value = defense_cross(
        red_two_moat_stats, red_two_moat_miss_stats)
    red_two_moat_stuck_stats = defense_stuck(
        red_two_moat_stats, red_two_moat_miss_stats, red_two_moat_stuck_stats)
    red_two_sallyp_stats_value = defense_cross(
        red_two_sallyp_stats, red_two_sallyp_miss_stats)
    red_two_sallyp_stuck_stats = defense_stuck(
        red_two_sallyp_stats, red_two_sallyp_miss_stats, red_two_sallyp_stuck_stats)
    red_two_rought_stats_value = defense_cross(
        red_two_rought_stats, red_two_rought_miss_stats)
    red_two_rought_stuck_stats = defense_stuck(
        red_two_rought_stats, red_two_rought_miss_stats, red_two_rought_stuck_stats)
    red_two_lowbar_stats_value = defense_cross(
        red_two_lowbar_stats, red_two_lowbar_miss_stats)
    red_two_lowbar_stuck_stats = defense_stuck(
        red_two_lowbar_stats, red_two_lowbar_miss_stats, red_two_lowbar_stuck_stats)
    red_two_ramparts_stats_value = defense_cross(
        red_two_ramparts_stats, red_two_ramparts_miss_stats)
    red_two_ramparts_stuck_stats = defense_stuck(
        red_two_ramparts_stats, red_two_ramparts_miss_stats, red_two_ramparts_stuck_stats)
    red_two_rockwall_stats_value = defense_cross(
        red_two_rockwall_stats, red_two_rockwall_miss_stats)
    red_two_rockwall_stuck_stats = defense_stuck(
        red_two_rockwall_stats, red_two_rockwall_miss_stats, red_two_rockwall_stuck_stats)
    red_two_hang_success_stats = hang_succes(
        red_two_hang_input_values, red_two_hang_success_values)
    red_two_played_def_stats = played_def(red_two_played_def_values)
    red_two_hang_value = hang_total(
        red_two_hang_input_values, red_two_hang_success_values, red_two_hang_fail_values)
    red_two_hang_fail = hang_fail(
        red_two_hang_input_values, red_two_hang_fail_values)
    red_two_auton_low_stats = auto_lows(red_two_auton_low_values)
    red_two_auton_high_stats = auto_highs(red_two_auton_high_values)
    red_two_teleop_low_stats = teleop_lows(red_two_teleop_low_values)
    red_two_teleop_high_stats = teleop_highs(red_two_teleop_high_values)

    for match in red_three_matches:
        red_three_auton_low_values.append(match.auton_low_goals)
        red_three_auton_high_values.append(match.auton_high_goals)
        red_three_teleop_low_values.append(match.teleop_low_goals)
        red_three_teleop_high_values.append(match.teleop_high_goals)
        red_three_auton_def_reached_values.append(match.auton_def_reached)
        red_three_auton_def_crossed_values.append(match.auton_def_crossed)
        red_three_played_def_values.append(match.played_def)
        if match.hang_input == 1:
            red_three_hang_input_values.append(match.hang_input)
        elif match.hang_input == 2:
            red_three_hang_success_values.append(match.hang_input)
        else:
            red_three_hang_fail_values.append(match.hang_input)
        if match.teleop_portc == 1:
            red_three_portc_stuck_stats.append(match.teleop_portc)
        elif match.teleop_portc == 4:
            red_three_portc_miss_stats.append(match.teleop_portc)
        elif match.teleop_portc != 0:
            red_three_portc_stats.append(match.teleop_portc)
        else:
            pass
        if match.teleop_drawb == 1:
            red_three_drawb_stuck_stats.append(match.teleop_drawb)
        elif match.teleop_drawb == 4:
            red_three_drawb_miss_stats.append(match.teleop_drawb)
        elif match.teleop_drawb != 0:
            red_three_drawb_stats.append(match.teleop_drawb)
        else:
            pass
        if match.teleop_cdf == 1:
            red_three_cdf_stuck_stats.append(match.teleop_cdf)
        elif match.teleop_cdf == 4:
            red_three_cdf_miss_stats.append(match.teleop_cdf)
        elif match.teleop_cdf != 0:
            red_three_cdf_stats.append(match.teleop_cdf)
        else:
            pass
        if match.teleop_moat == 1:
            red_three_moat_stuck_stats.append(match.teleop_moat)
        elif match.teleop_moat == 4:
            red_three_moat_miss_stats.append(match.teleop_moat)
        elif match.teleop_moat != 0:
            red_three_moat_stats.append(match.teleop_moat)
        else:
            pass
        if match.teleop_sallyp == 1:
            red_three_sallyp_stuck_stats.append(match.teleop_sallyp)
        elif match.teleop_sallyp == 4:
            red_three_sallyp_miss_stats.append(match.teleop_sallyp)
        elif match.teleop_sallyp != 0:
            red_three_sallyp_stats.append(match.teleop_sallyp)
        else:
            pass
        if match.teleop_rought == 1:
            red_three_rought_stuck_stats.append(match.teleop_rought)
        elif match.teleop_rought == 4:
            red_three_rought_miss_stats.append(match.teleop_rought)
        elif match.teleop_rought != 0:
            red_three_rought_stats.append(match.teleop_rought)
        else:
            pass
        if match.teleop_lowbar == 1:
            red_three_lowbar_stuck_stats.append(match.teleop_lowbar)
        elif match.teleop_lowbar == 4:
            red_three_lowbar_miss_stats.append(match.teleop_lowbar)
        elif match.teleop_lowbar != 0:
            red_three_lowbar_stats.append(match.teleop_lowbar)
        else:
            pass
        if match.teleop_ramparts == 1:
            red_three_ramparts_stuck_stats.append(match.teleop_ramparts)
        elif match.teleop_ramparts == 4:
            red_three_ramparts_miss_stats.append(match.teleop_ramparts)
        elif match.teleop_ramparts != 0:
            red_three_ramparts_stats.append(match.teleop_ramparts)
        else:
            pass
        if match.teleop_rockwall == 1:
            red_three_rockwall_stuck_stats.append(match.teleop_rockwall)
        elif match.teleop_rockwall == 4:
            red_three_rockwall_miss_stats.append(match.teleop_rockwall)
        elif match.teleop_rockwall != 0:
            red_three_rockwall_stats.append(match.teleop_rockwall)
        else:
            pass
    red_three_portc_stats_value = defense_cross(
        red_three_portc_stats, red_three_portc_miss_stats)
    red_three_portc_stuck_stats = defense_stuck(
        red_three_portc_stats, red_three_portc_miss_stats, red_three_portc_stuck_stats)
    red_three_drawb_stats_value = defense_cross(
        red_three_drawb_stats, red_three_drawb_miss_stats)
    red_three_drawb_stuck_stats = defense_stuck(
        red_three_drawb_stats, red_three_drawb_miss_stats, red_three_drawb_stuck_stats)
    red_three_cdf_stats_value = defense_cross(
        red_three_cdf_stats, red_three_cdf_miss_stats)
    red_three_cdf_stuck_stats = defense_stuck(
        red_three_cdf_stats, red_three_cdf_miss_stats, red_three_cdf_stuck_stats)
    red_three_moat_stats_value = defense_cross(
        red_three_moat_stats, red_three_moat_miss_stats)
    red_three_moat_stuck_stats = defense_stuck(
        red_three_moat_stats, red_three_moat_miss_stats, red_three_moat_stuck_stats)
    red_three_sallyp_stats_value = defense_cross(
        red_three_sallyp_stats, red_three_sallyp_miss_stats)
    red_three_sallyp_stuck_stats = defense_stuck(
        red_three_sallyp_stats, red_three_sallyp_miss_stats, red_three_sallyp_stuck_stats)
    red_three_rought_stats_value = defense_cross(
        red_three_rought_stats, red_three_rought_miss_stats)
    red_three_rought_stuck_stats = defense_stuck(
        red_three_rought_stats, red_three_rought_miss_stats, red_three_rought_stuck_stats)
    red_three_lowbar_stats_value = defense_cross(
        red_three_lowbar_stats, red_three_lowbar_miss_stats)
    red_three_lowbar_stuck_stats = defense_stuck(
        red_three_lowbar_stats, red_three_lowbar_miss_stats, red_three_lowbar_stuck_stats)
    red_three_ramparts_stats_value = defense_cross(
        red_three_ramparts_stats, red_three_ramparts_miss_stats)
    red_three_ramparts_stuck_stats = defense_stuck(
        red_three_ramparts_stats, red_three_ramparts_miss_stats, red_three_ramparts_stuck_stats)
    red_three_rockwall_stats_value = defense_cross(
        red_three_rockwall_stats, red_three_rockwall_miss_stats)
    red_three_rockwall_stuck_stats = defense_stuck(
        red_three_rockwall_stats, red_three_rockwall_miss_stats, red_three_rockwall_stuck_stats)
    red_three_hang_success_stats = hang_succes(
        red_three_hang_input_values, red_three_hang_success_values)
    red_three_played_def_stats = played_def(red_three_played_def_values)
    red_three_hang_value = hang_total(
        red_three_hang_input_values, red_three_hang_success_values, red_three_hang_fail_values)
    red_three_hang_fail = hang_fail(
        red_three_hang_input_values, red_three_hang_fail_values)
    red_three_auton_low_stats = auto_lows(red_three_auton_low_values)
    red_three_auton_high_stats = auto_highs(red_three_auton_high_values)
    red_three_teleop_low_stats = teleop_lows(red_three_teleop_low_values)
    red_three_teleop_high_stats = teleop_highs(red_three_teleop_high_values)

    for match in blue_one_matches:
        blue_one_auton_low_values.append(match.auton_low_goals)
        blue_one_auton_high_values.append(match.auton_high_goals)
        blue_one_teleop_low_values.append(match.teleop_low_goals)
        blue_one_teleop_high_values.append(match.teleop_high_goals)
        blue_one_auton_def_reached_values.append(match.auton_def_reached)
        blue_one_auton_def_crossed_values.append(match.auton_def_crossed)
        blue_one_played_def_values.append(match.played_def)
        if match.hang_input == 1:
            blue_one_hang_input_values.append(match.hang_input)
        elif match.hang_input == 2:
            blue_one_hang_success_values.append(match.hang_input)
        else:
            blue_one_hang_fail_values.append(match.hang_input)
        if match.teleop_portc == 1:
            blue_one_portc_stuck_stats.append(match.teleop_portc)
        elif match.teleop_portc == 4:
            blue_one_portc_miss_stats.append(match.teleop_portc)
        elif match.teleop_portc != 0:
            blue_one_portc_stats.append(match.teleop_portc)
        else:
            pass
        if match.teleop_drawb == 1:
            blue_one_drawb_stuck_stats.append(match.teleop_drawb)
        elif match.teleop_drawb == 4:
            blue_one_drawb_miss_stats.append(match.teleop_drawb)
        elif match.teleop_drawb != 0:
            blue_one_drawb_stats.append(match.teleop_drawb)
        else:
            pass
        if match.teleop_cdf == 1:
            blue_one_cdf_stuck_stats.append(match.teleop_cdf)
        elif match.teleop_cdf == 4:
            blue_one_cdf_miss_stats.append(match.teleop_cdf)
        elif match.teleop_cdf != 0:
            blue_one_cdf_stats.append(match.teleop_cdf)
        else:
            pass
        if match.teleop_moat == 1:
            blue_one_moat_stuck_stats.append(match.teleop_moat)
        elif match.teleop_moat == 4:
            blue_one_moat_miss_stats.append(match.teleop_moat)
        elif match.teleop_moat != 0:
            blue_one_moat_stats.append(match.teleop_moat)
        else:
            pass
        if match.teleop_sallyp == 1:
            blue_one_sallyp_stuck_stats.append(match.teleop_sallyp)
        elif match.teleop_sallyp == 4:
            blue_one_sallyp_miss_stats.append(match.teleop_sallyp)
        elif match.teleop_sallyp != 0:
            blue_one_sallyp_stats.append(match.teleop_sallyp)
        else:
            pass
        if match.teleop_rought == 1:
            blue_one_rought_stuck_stats.append(match.teleop_rought)
        elif match.teleop_rought == 4:
            blue_one_rought_miss_stats.append(match.teleop_rought)
        elif match.teleop_rought != 0:
            blue_one_rought_stats.append(match.teleop_rought)
        else:
            pass
        if match.teleop_lowbar == 1:
            blue_one_lowbar_stuck_stats.append(match.teleop_lowbar)
        elif match.teleop_lowbar == 4:
            blue_one_lowbar_miss_stats.append(match.teleop_lowbar)
        elif match.teleop_lowbar != 0:
            blue_one_lowbar_stats.append(match.teleop_lowbar)
        else:
            pass
        if match.teleop_ramparts == 1:
            blue_one_ramparts_stuck_stats.append(match.teleop_ramparts)
        elif match.teleop_ramparts == 4:
            blue_one_ramparts_miss_stats.append(match.teleop_ramparts)
        elif match.teleop_ramparts != 0:
            blue_one_ramparts_stats.append(match.teleop_ramparts)
        else:
            pass
        if match.teleop_rockwall == 1:
            blue_one_rockwall_stuck_stats.append(match.teleop_rockwall)
        elif match.teleop_rockwall == 4:
            blue_one_rockwall_miss_stats.append(match.teleop_rockwall)
        elif match.teleop_rockwall != 0:
            blue_one_rockwall_stats.append(match.teleop_rockwall)
        else:
            pass
    blue_one_portc_stats_value = defense_cross(
        blue_one_portc_stats, blue_one_portc_miss_stats)
    blue_one_portc_stuck_stats = defense_stuck(
        blue_one_portc_stats, blue_one_portc_miss_stats, blue_one_portc_stuck_stats)
    blue_one_drawb_stats_value = defense_cross(
        blue_one_drawb_stats, blue_one_drawb_miss_stats)
    blue_one_drawb_stuck_stats = defense_stuck(
        blue_one_drawb_stats, blue_one_drawb_miss_stats, blue_one_drawb_stuck_stats)
    blue_one_cdf_stats_value = defense_cross(
        blue_one_cdf_stats, blue_one_cdf_miss_stats)
    blue_one_cdf_stuck_stats = defense_stuck(
        blue_one_cdf_stats, blue_one_cdf_miss_stats, blue_one_cdf_stuck_stats)
    blue_one_moat_stats_value = defense_cross(
        blue_one_moat_stats, blue_one_moat_miss_stats)
    blue_one_moat_stuck_stats = defense_stuck(
        blue_one_moat_stats, blue_one_moat_miss_stats, blue_one_moat_stuck_stats)
    blue_one_sallyp_stats_value = defense_cross(
        blue_one_sallyp_stats, blue_one_sallyp_miss_stats)
    blue_one_sallyp_stuck_stats = defense_stuck(
        blue_one_sallyp_stats, blue_one_sallyp_miss_stats, blue_one_sallyp_stuck_stats)
    blue_one_rought_stats_value = defense_cross(
        blue_one_rought_stats, blue_one_rought_miss_stats)
    blue_one_rought_stuck_stats = defense_stuck(
        blue_one_rought_stats, blue_one_rought_miss_stats, blue_one_rought_stuck_stats)
    blue_one_lowbar_stats_value = defense_cross(
        blue_one_lowbar_stats, blue_one_lowbar_miss_stats)
    blue_one_lowbar_stuck_stats = defense_stuck(
        blue_one_lowbar_stats, blue_one_lowbar_miss_stats, blue_one_lowbar_stuck_stats)
    blue_one_ramparts_stats_value = defense_cross(
        blue_one_ramparts_stats, blue_one_ramparts_miss_stats)
    blue_one_ramparts_stuck_stats = defense_stuck(
        blue_one_ramparts_stats, blue_one_ramparts_miss_stats, blue_one_ramparts_stuck_stats)
    blue_one_rockwall_stats_value = defense_cross(
        blue_one_rockwall_stats, blue_one_rockwall_miss_stats)
    blue_one_rockwall_stuck_stats = defense_stuck(
        blue_one_rockwall_stats, blue_one_rockwall_miss_stats, blue_one_rockwall_stuck_stats)
    blue_one_hang_success_stats = hang_succes(
        blue_one_hang_input_values, blue_one_hang_success_values)
    blue_one_played_def_stats = played_def(blue_one_played_def_values)
    blue_one_hang_value = hang_total(
        blue_one_hang_input_values, blue_one_hang_success_values, blue_one_hang_fail_values)
    blue_one_hang_fail = hang_fail(
        blue_one_hang_input_values, blue_one_hang_fail_values)
    blue_one_auton_low_stats = auto_lows(blue_one_auton_low_values)
    blue_one_auton_high_stats = auto_highs(blue_one_auton_high_values)
    blue_one_teleop_low_stats = teleop_lows(blue_one_teleop_low_values)
    blue_one_teleop_high_stats = teleop_highs(blue_one_teleop_high_values)

    for match in blue_two_matches:
        blue_two_auton_low_values.append(match.auton_low_goals)
        blue_two_auton_high_values.append(match.auton_high_goals)
        blue_two_teleop_low_values.append(match.teleop_low_goals)
        blue_two_teleop_high_values.append(match.teleop_high_goals)
        blue_two_auton_def_reached_values.append(match.auton_def_reached)
        blue_two_auton_def_crossed_values.append(match.auton_def_crossed)
        blue_two_played_def_values.append(match.played_def)
        if match.hang_input == 1:
            blue_two_hang_input_values.append(match.hang_input)
        elif match.hang_input == 2:
            blue_two_hang_success_values.append(match.hang_input)
        else:
            blue_two_hang_fail_values.append(match.hang_input)
        if match.teleop_portc == 1:
            blue_two_portc_stuck_stats.append(match.teleop_portc)
        elif match.teleop_portc == 4:
            blue_two_portc_miss_stats.append(match.teleop_portc)
        elif match.teleop_portc != 0:
            blue_two_portc_stats.append(match.teleop_portc)
        else:
            pass
        if match.teleop_drawb == 1:
            blue_two_drawb_stuck_stats.append(match.teleop_drawb)
        elif match.teleop_drawb == 4:
            blue_two_drawb_miss_stats.append(match.teleop_drawb)
        elif match.teleop_drawb != 0:
            blue_two_drawb_stats.append(match.teleop_drawb)
        else:
            pass
        if match.teleop_cdf == 1:
            blue_two_cdf_stuck_stats.append(match.teleop_cdf)
        elif match.teleop_cdf == 4:
            blue_two_cdf_miss_stats.append(match.teleop_cdf)
        elif match.teleop_cdf != 0:
            blue_two_cdf_stats.append(match.teleop_cdf)
        else:
            pass
        if match.teleop_moat == 1:
            blue_two_moat_stuck_stats.append(match.teleop_moat)
        elif match.teleop_moat == 4:
            blue_two_moat_miss_stats.append(match.teleop_moat)
        elif match.teleop_moat != 0:
            blue_two_moat_stats.append(match.teleop_moat)
        else:
            pass
        if match.teleop_sallyp == 1:
            blue_two_sallyp_stuck_stats.append(match.teleop_sallyp)
        elif match.teleop_sallyp == 4:
            blue_two_sallyp_miss_stats.append(match.teleop_sallyp)
        elif match.teleop_sallyp != 0:
            blue_two_sallyp_stats.append(match.teleop_sallyp)
        else:
            pass
        if match.teleop_rought == 1:
            blue_two_rought_stuck_stats.append(match.teleop_rought)
        elif match.teleop_rought == 4:
            blue_two_rought_miss_stats.append(match.teleop_rought)
        elif match.teleop_rought != 0:
            blue_two_rought_stats.append(match.teleop_rought)
        else:
            pass
        if match.teleop_lowbar == 1:
            blue_two_lowbar_stuck_stats.append(match.teleop_lowbar)
        elif match.teleop_lowbar == 4:
            blue_two_lowbar_miss_stats.append(match.teleop_lowbar)
        elif match.teleop_lowbar != 0:
            blue_two_lowbar_stats.append(match.teleop_lowbar)
        else:
            pass
        if match.teleop_ramparts == 1:
            blue_two_ramparts_stuck_stats.append(match.teleop_ramparts)
        elif match.teleop_ramparts == 4:
            blue_two_ramparts_miss_stats.append(match.teleop_ramparts)
        elif match.teleop_ramparts != 0:
            blue_two_ramparts_stats.append(match.teleop_ramparts)
        else:
            pass
        if match.teleop_rockwall == 1:
            blue_two_rockwall_stuck_stats.append(match.teleop_rockwall)
        elif match.teleop_rockwall == 4:
            blue_two_rockwall_miss_stats.append(match.teleop_rockwall)
        elif match.teleop_rockwall != 0:
            blue_two_rockwall_stats.append(match.teleop_rockwall)
        else:
            pass
    blue_two_portc_stats_value = defense_cross(
        blue_two_portc_stats, blue_two_portc_miss_stats)
    blue_two_portc_stuck_stats = defense_stuck(
        blue_two_portc_stats, blue_two_portc_miss_stats, blue_two_portc_stuck_stats)
    blue_two_drawb_stats_value = defense_cross(
        blue_two_drawb_stats, blue_two_drawb_miss_stats)
    blue_two_drawb_stuck_stats = defense_stuck(
        blue_two_drawb_stats, blue_two_drawb_miss_stats, blue_two_drawb_stuck_stats)
    blue_two_cdf_stats_value = defense_cross(
        blue_two_cdf_stats, blue_two_cdf_miss_stats)
    blue_two_cdf_stuck_stats = defense_stuck(
        blue_two_cdf_stats, blue_two_cdf_miss_stats, blue_two_cdf_stuck_stats)
    blue_two_moat_stats_value = defense_cross(
        blue_two_moat_stats, blue_two_moat_miss_stats)
    blue_two_moat_stuck_stats = defense_stuck(
        blue_two_moat_stats, blue_two_moat_miss_stats, blue_two_moat_stuck_stats)
    blue_two_sallyp_stats_value = defense_cross(
        blue_two_sallyp_stats, blue_two_sallyp_miss_stats)
    blue_two_sallyp_stuck_stats = defense_stuck(
        blue_two_sallyp_stats, blue_two_sallyp_miss_stats, blue_two_sallyp_stuck_stats)
    blue_two_rought_stats_value = defense_cross(
        blue_two_rought_stats, blue_two_rought_miss_stats)
    blue_two_rought_stuck_stats = defense_stuck(
        blue_two_rought_stats, blue_two_rought_miss_stats, blue_two_rought_stuck_stats)
    blue_two_lowbar_stats_value = defense_cross(
        blue_two_lowbar_stats, blue_two_lowbar_miss_stats)
    blue_two_lowbar_stuck_stats = defense_stuck(
        blue_two_lowbar_stats, blue_two_lowbar_miss_stats, blue_two_lowbar_stuck_stats)
    blue_two_ramparts_stats_value = defense_cross(
        blue_two_ramparts_stats, blue_two_ramparts_miss_stats)
    blue_two_ramparts_stuck_stats = defense_stuck(
        blue_two_ramparts_stats, blue_two_ramparts_miss_stats, blue_two_ramparts_stuck_stats)
    blue_two_rockwall_stats_value = defense_cross(
        blue_two_rockwall_stats, blue_two_rockwall_miss_stats)
    blue_two_rockwall_stuck_stats = defense_stuck(
        blue_two_rockwall_stats, blue_two_rockwall_miss_stats, blue_two_rockwall_stuck_stats)
    blue_two_hang_success_stats = hang_succes(
        blue_two_hang_input_values, blue_two_hang_success_values)
    blue_two_played_def_stats = played_def(blue_two_played_def_values)
    blue_two_hang_value = hang_total(
        blue_two_hang_input_values, blue_two_hang_success_values, blue_two_hang_fail_values)
    blue_two_hang_fail = hang_fail(
        blue_two_hang_input_values, blue_two_hang_fail_values)
    blue_two_auton_low_stats = auto_lows(blue_two_auton_low_values)
    blue_two_auton_high_stats = auto_highs(blue_two_auton_high_values)
    blue_two_teleop_low_stats = teleop_lows(blue_two_teleop_low_values)
    blue_two_teleop_high_stats = teleop_highs(blue_two_teleop_high_values)

    for match in blue_three_matches:
        blue_three_auton_low_values.append(match.auton_low_goals)
        blue_three_auton_high_values.append(match.auton_high_goals)
        blue_three_teleop_low_values.append(match.teleop_low_goals)
        blue_three_teleop_high_values.append(match.teleop_high_goals)
        blue_three_auton_def_reached_values.append(match.auton_def_reached)
        blue_three_auton_def_crossed_values.append(match.auton_def_crossed)
        blue_three_played_def_values.append(match.played_def)
        if match.hang_input == 1:
            blue_three_hang_input_values.append(match.hang_input)
        elif match.hang_input == 2:
            blue_three_hang_success_values.append(match.hang_input)
        else:
            blue_three_hang_fail_values.append(match.hang_input)
        if match.teleop_portc == 1:
            blue_three_portc_stuck_stats.append(match.teleop_portc)
        elif match.teleop_portc == 4:
            blue_three_portc_miss_stats.append(match.teleop_portc)
        elif match.teleop_portc != 0:
            blue_three_portc_stats.append(match.teleop_portc)
        else:
            pass
        if match.teleop_drawb == 1:
            blue_three_drawb_stuck_stats.append(match.teleop_drawb)
        elif match.teleop_drawb == 4:
            blue_three_drawb_miss_stats.append(match.teleop_drawb)
        elif match.teleop_drawb != 0:
            blue_three_drawb_stats.append(match.teleop_drawb)
        else:
            pass
        if match.teleop_cdf == 1:
            blue_three_cdf_stuck_stats.append(match.teleop_cdf)
        elif match.teleop_cdf == 4:
            blue_three_cdf_miss_stats.append(match.teleop_cdf)
        elif match.teleop_cdf != 0:
            blue_three_cdf_stats.append(match.teleop_cdf)
        else:
            pass
        if match.teleop_moat == 1:
            blue_three_moat_stuck_stats.append(match.teleop_moat)
        elif match.teleop_moat == 4:
            blue_three_moat_miss_stats.append(match.teleop_moat)
        elif match.teleop_moat != 0:
            blue_three_moat_stats.append(match.teleop_moat)
        else:
            pass
        if match.teleop_sallyp == 1:
            blue_three_sallyp_stuck_stats.append(match.teleop_sallyp)
        elif match.teleop_sallyp == 4:
            blue_three_sallyp_miss_stats.append(match.teleop_sallyp)
        elif match.teleop_sallyp != 0:
            blue_three_sallyp_stats.append(match.teleop_sallyp)
        else:
            pass
        if match.teleop_rought == 1:
            blue_three_rought_stuck_stats.append(match.teleop_rought)
        elif match.teleop_rought == 4:
            blue_three_rought_miss_stats.append(match.teleop_rought)
        elif match.teleop_rought != 0:
            blue_three_rought_stats.append(match.teleop_rought)
        else:
            pass
        if match.teleop_lowbar == 1:
            blue_three_lowbar_stuck_stats.append(match.teleop_lowbar)
        elif match.teleop_lowbar == 4:
            blue_three_lowbar_miss_stats.append(match.teleop_lowbar)
        elif match.teleop_lowbar != 0:
            blue_three_lowbar_stats.append(match.teleop_lowbar)
        else:
            pass
        if match.teleop_ramparts == 1:
            blue_three_ramparts_stuck_stats.append(match.teleop_ramparts)
        elif match.teleop_ramparts == 4:
            blue_three_ramparts_miss_stats.append(match.teleop_ramparts)
        elif match.teleop_ramparts != 0:
            blue_three_ramparts_stats.append(match.teleop_ramparts)
        else:
            pass
        if match.teleop_rockwall == 1:
            blue_three_rockwall_stuck_stats.append(match.teleop_rockwall)
        elif match.teleop_rockwall == 4:
            blue_three_rockwall_miss_stats.append(match.teleop_rockwall)
        elif match.teleop_rockwall != 0:
            blue_three_rockwall_stats.append(match.teleop_rockwall)
        else:
            pass
    blue_three_portc_stats_value = defense_cross(
        blue_three_portc_stats, blue_three_portc_miss_stats)
    blue_three_portc_stuck_stats = defense_stuck(
        blue_three_portc_stats, blue_three_portc_miss_stats, blue_three_portc_stuck_stats)
    blue_three_drawb_stats_value = defense_cross(
        blue_three_drawb_stats, blue_three_drawb_miss_stats)
    blue_three_drawb_stuck_stats = defense_stuck(
        blue_three_drawb_stats, blue_three_drawb_miss_stats, blue_three_drawb_stuck_stats)
    blue_three_cdf_stats_value = defense_cross(
        blue_three_cdf_stats, blue_three_cdf_miss_stats)
    blue_three_cdf_stuck_stats = defense_stuck(
        blue_three_cdf_stats, blue_three_cdf_miss_stats, blue_three_cdf_stuck_stats)
    blue_three_moat_stats_value = defense_cross(
        blue_three_moat_stats, blue_three_moat_miss_stats)
    blue_three_moat_stuck_stats = defense_stuck(
        blue_three_moat_stats, blue_three_moat_miss_stats, blue_three_moat_stuck_stats)
    blue_three_sallyp_stats_value = defense_cross(
        blue_three_sallyp_stats, blue_three_sallyp_miss_stats)
    blue_three_sallyp_stuck_stats = defense_stuck(
        blue_three_sallyp_stats, blue_three_sallyp_miss_stats, blue_three_sallyp_stuck_stats)
    blue_three_rought_stats_value = defense_cross(
        blue_three_rought_stats, blue_three_rought_miss_stats)
    blue_three_rought_stuck_stats = defense_stuck(
        blue_three_rought_stats, blue_three_rought_miss_stats, blue_three_rought_stuck_stats)
    blue_three_lowbar_stats_value = defense_cross(
        blue_three_lowbar_stats, blue_three_lowbar_miss_stats)
    blue_three_lowbar_stuck_stats = defense_stuck(
        blue_three_lowbar_stats, blue_three_lowbar_miss_stats, blue_three_lowbar_stuck_stats)
    blue_three_ramparts_stats_value = defense_cross(
        blue_three_ramparts_stats, blue_three_ramparts_miss_stats)
    blue_three_ramparts_stuck_stats = defense_stuck(
        blue_three_ramparts_stats, blue_three_ramparts_miss_stats, blue_three_ramparts_stuck_stats)
    blue_three_rockwall_stats_value = defense_cross(
        blue_three_rockwall_stats, blue_three_rockwall_miss_stats)
    blue_three_rockwall_stuck_stats = defense_stuck(
        blue_three_rockwall_stats, blue_three_rockwall_miss_stats, blue_three_rockwall_stuck_stats)
    blue_three_hang_success_stats = hang_succes(
        blue_three_hang_input_values, blue_three_hang_success_values)
    blue_three_played_def_stats = played_def(blue_three_played_def_values)
    blue_three_hang_value = hang_total(
        blue_three_hang_input_values, blue_three_hang_success_values, blue_three_hang_fail_values)
    blue_three_hang_fail = hang_fail(
        blue_three_hang_input_values, blue_three_hang_fail_values)
    blue_three_auton_low_stats = auto_lows(blue_three_auton_low_values)
    blue_three_auton_high_stats = auto_highs(blue_three_auton_high_values)
    blue_three_teleop_low_stats = teleop_lows(blue_three_teleop_low_values)
    blue_three_teleop_high_stats = teleop_highs(blue_three_teleop_high_values)

    # next step is to develop actual scores from data about teams
    red_score = []
    blue_score = []

    def auto_goal_score(low, high):
        low_num = round(low)
        high_num = round(high)
        goal_random = random.random()
        if goal_random >= .5:
            return high_num * 10
        else:
            return low_num * 5

    def teleop_goal_score(low, high):
        low_num = round(low)
        high_num = round(high)
        low_random = random.random()
        high_random = random.random()
        if low_random >= .85:
            low_num = round(low_num * 1.25)
        elif low_random >= .75:
            low_num = low_num
        elif low_random >= .5:
            low_num = round(low_num * .75)
        elif low_random >= .25:
            low_num = round(low_num * .6)
        else:
            low_num = round(low_num * .35)
        if high_random >= .85:
            high_num = round(high_num * 1.25)
        elif high_random >= .75:
            high_num = high_num
        elif high_random >= .5:
            high_num = round(high_num * .75)
        elif high_random >= .25:
            high_num = round(high_num * .6)
        else:
            high_num = round(high_num * .35)
        return (low_num * 2) + (high_num * 5)

    def auto_def_score(reach, cross):
        if len(cross) > 0:
            return 10
        elif len(reach) > 0:
            return 2
        else:
            return 0

    def hang_score(success_one, total_one, success_two, total_two, success_three, total_three):
        one = random.random()
        two = random.random()
        three = random.random()
        if one < success_one:
            one_score = 15
        elif one < total_one:
            one_score = 5
        else:
            one_score = 0
        if two < success_two:
            two_score = 15
        elif two < total_two:
            two_score = 5
        else:
            two_score = 0
        if three < success_three:
            three_score = 15
        elif three < total_three:
            three_score = 5
        else:
            three_score = 0
        if one_score > 0 and two_score > 0 and three_score > 0:
            capture = 25
        else:
            capture = 0
        hang_score_totals = one_score + two_score + three_score + capture
        return hang_score_totals

    def breach_scoring(one_portc_stats_value,
                       one_drawb_stats_value,
                       one_cdf_stats_value,
                       one_moat_stats_value,
                       one_sallyp_stats_value,
                       one_rought_stats_value,
                       one_lowbar_stats_value,
                       one_ramparts_stats_value,
                       one_rockwall_stats_value,
                       two_portc_stats_value,
                       two_drawb_stats_value,
                       two_cdf_stats_value,
                       two_moat_stats_value,
                       two_sallyp_stats_value,
                       two_rought_stats_value,
                       two_lowbar_stats_value,
                       two_ramparts_stats_value,
                       two_rockwall_stats_value,
                       three_portc_stats_value,
                       three_drawb_stats_value,
                       three_cdf_stats_value,
                       three_moat_stats_value,
                       three_sallyp_stats_value,
                       three_rought_stats_value,
                       three_lowbar_stats_value,
                       three_ramparts_stats_value,
                       three_rockwall_stats_value):

        def_a = ['cheval de frise', 'portcullis']
        def_b = ['moat', 'ramparts']
        def_c = ['drawbridge', 'sallyport']
        def_d = ['rockwall', 'rough terrain']
        def_one = random.choice(def_a)
        def_two = random.choice(def_b)
        def_three = random.choice(def_c)
        def_four = random.choice(def_d)
        lowbar_math = random.randint(1, 4)
        lowbar_avg = round(one_lowbar_stats_value) + \
            round(two_lowbar_stats_value) + round(three_lowbar_stats_value)
        lowbar_total = lowbar_avg / lowbar_math
        sallyp_score = 0
        lowbar_score = 0
        portc_score = 0
        ramparts_score = 0
        rought_score = 0
        cdf_score = 0
        drawb_score = 0
        moat_score = 0
        rockwall_score = 0
        if lowbar_total > 2:
            lowbar_score = 10
        elif lowbar_total > 1:
            lowbar_score = 5
        else:
            lowbar_score = 0
        if def_one == 'cheval de frise':
            math = random.randint(1, 4)
            cdf_avg = round(one_cdf_stats_value) + \
                round(two_cdf_stats_value) + round(three_cdf_stats_value)
            cdf_total = cdf_avg / math
            if cdf_total >= 2:
                cdf_score = 10
            elif cdf_total >= 1:
                cdf_score = 5
            else:
                cdf_score = 0
        else:
            math = random.randint(1, 4)
            portc_avg = round(one_portc_stats_value) + \
                round(two_portc_stats_value) + round(three_portc_stats_value)
            portc_total = portc_avg / math
            if portc_total >= 2:
                portc_score = 10
            elif portc_total >= 1:
                portc_score = 5
            else:
                portc_score = 0
        if def_two == 'moat':
            math = random.randint(1, 4)
            moat_avg = round(one_moat_stats_value) + \
                round(two_moat_stats_value) + round(three_moat_stats_value)
            moat_total = moat_avg / math
            if moat_total >= 2:
                moat_score = 10
            elif moat_total >= 1:
                moat_score = 5
            else:
                moat_score = 0
        else:
            math = random.randint(1, 4)
            ramparts_avg = round(one_ramparts_stats_value) + round(
                two_ramparts_stats_value) + round(three_ramparts_stats_value)
            ramparts_total = ramparts_avg / math
            if ramparts_total >= 2:
                ramparts_score = 10
            elif ramparts_total >= 1:
                ramparts_score = 5
            else:
                ramparts_score = 0
        if def_three == 'drawbridge':
            math = random.randint(1, 4)
            drawb_avg = round(one_drawb_stats_value) + \
                round(two_drawb_stats_value) + round(three_drawb_stats_value)
            drawb_total = drawb_avg / math
            if drawb_total >= 2:
                drawb_score = 10
            elif drawb_total >= 1:
                drawb_score = 5
            else:
                drawb_score = 0
        else:
            math = random.randint(1, 4)
            sallyp_avg = round(one_sallyp_stats_value) + \
                round(two_sallyp_stats_value) + round(three_sallyp_stats_value)
            sallyp_total = sallyp_avg / math
            if sallyp_total >= 2:
                sallyp_score = 10
            elif sallyp_total >= 1:
                sallyp_score = 5
            else:
                sallyp_score = 0
        if def_four == 'rockwall':
            rockwall_total = round(one_rockwall_stats_value) + round(
                two_rockwall_stats_value) + round(three_rockwall_stats_value)
            if rockwall_total >= 2:
                rockwall_score = 10
            elif rockwall_total >= 1:
                rockwall_score = 5
            else:
                rockwall_score = 0
        else:
            rought_total = round(one_rought_stats_value) + \
                round(two_rought_stats_value) + round(three_rought_stats_value)
            if rought_total >= 2:
                rought_score = 10
            elif rought_total >= 1:
                rought_score = 5
            else:
                rought_score = 0
        defense_total = (lowbar_score + cdf_score + portc_score + moat_score +
                         ramparts_score + drawb_score + sallyp_score + rockwall_score + rought_score)
        if defense_total >= 40:
            breach_confirm = 'BREACH'
        else:
            breach_confirm = 'NO BREACH'
        return defense_total, breach_confirm, def_one, def_two, def_three, def_four

    red_score.append(auto_goal_score(
        red_one_auton_low_stats, red_one_auton_high_stats))
    red_score.append(teleop_goal_score(
        red_one_teleop_low_stats, red_one_teleop_high_stats))
    red_score.append(auto_def_score(
        red_one_auton_def_reached_values, red_one_auton_def_crossed_values))
    red_score.append(auto_goal_score(
        red_two_auton_low_stats, red_two_auton_high_stats))
    red_score.append(teleop_goal_score(
        red_two_teleop_low_stats, red_two_teleop_high_stats))
    red_score.append(auto_def_score(
        red_two_auton_def_reached_values, red_two_auton_def_crossed_values))
    red_score.append(auto_goal_score(
        red_three_auton_low_stats, red_three_auton_high_stats))
    red_score.append(teleop_goal_score(
        red_three_teleop_low_stats, red_three_teleop_high_stats))
    red_score.append(auto_def_score(
        red_three_auton_def_reached_values, red_three_auton_def_crossed_values))
    red_score.append(hang_score(red_one_hang_success_stats, red_one_hang_value,
                                red_two_hang_success_stats, red_two_hang_value,
                                red_three_hang_success_stats, red_three_hang_value))
    red_breach_info = breach_scoring(red_one_portc_stats_value,
                                     red_one_drawb_stats_value, red_one_cdf_stats_value,
                                     red_one_moat_stats_value, red_one_sallyp_stats_value,
                                     red_one_rought_stats_value, red_one_lowbar_stats_value,
                                     red_one_ramparts_stats_value, red_one_rockwall_stats_value,
                                     red_two_portc_stats_value, red_two_drawb_stats_value,
                                     red_two_cdf_stats_value, red_two_moat_stats_value,
                                     red_two_sallyp_stats_value, red_two_rought_stats_value,
                                     red_two_lowbar_stats_value, red_two_ramparts_stats_value,
                                     red_two_rockwall_stats_value, red_three_portc_stats_value,
                                     red_three_drawb_stats_value, red_three_cdf_stats_value,
                                     red_three_moat_stats_value, red_three_sallyp_stats_value,
                                     red_three_rought_stats_value, red_three_lowbar_stats_value,
                                     red_three_ramparts_stats_value, red_three_rockwall_stats_value)
    red_score.append(red_breach_info[0])
    blue_score.append(auto_goal_score(
        blue_one_auton_low_stats, blue_one_auton_high_stats))
    blue_score.append(teleop_goal_score(
        blue_one_teleop_low_stats, blue_one_teleop_high_stats))
    blue_score.append(auto_def_score(
        blue_one_auton_def_reached_values, blue_one_auton_def_crossed_values))
    blue_score.append(auto_goal_score(
        blue_two_auton_low_stats, blue_two_auton_high_stats))
    blue_score.append(teleop_goal_score(
        blue_two_teleop_low_stats, blue_two_teleop_high_stats))
    blue_score.append(auto_def_score(
        blue_two_auton_def_reached_values, blue_two_auton_def_crossed_values))
    blue_score.append(auto_goal_score(
        blue_three_auton_low_stats, blue_three_auton_high_stats))
    blue_score.append(teleop_goal_score(
        blue_three_teleop_low_stats, blue_three_teleop_high_stats))
    blue_score.append(auto_def_score(
        blue_three_auton_def_reached_values, blue_three_auton_def_crossed_values))
    blue_score.append(hang_score(
        blue_one_hang_success_stats, blue_one_hang_value,
        blue_two_hang_success_stats, blue_two_hang_value,
        blue_three_hang_success_stats, blue_three_hang_value))
    blue_breach_info = breach_scoring(
        blue_one_portc_stats_value, blue_one_drawb_stats_value,
        blue_one_cdf_stats_value, blue_one_moat_stats_value,
        blue_one_sallyp_stats_value, blue_one_rought_stats_value,
        blue_one_lowbar_stats_value, blue_one_ramparts_stats_value,
        blue_one_rockwall_stats_value, blue_two_portc_stats_value,
        blue_two_drawb_stats_value, blue_two_cdf_stats_value,
        blue_two_moat_stats_value, blue_two_sallyp_stats_value,
        blue_two_rought_stats_value, blue_two_lowbar_stats_value,
        blue_two_ramparts_stats_value, blue_two_rockwall_stats_value,
        blue_three_portc_stats_value, blue_three_drawb_stats_value,
        blue_three_cdf_stats_value, blue_three_moat_stats_value,
        blue_three_sallyp_stats_value, blue_three_rought_stats_value,
        blue_three_lowbar_stats_value, blue_three_ramparts_stats_value,
        blue_three_rockwall_stats_value)
    blue_score.append(blue_breach_info[0])

    red_score_total = int(sum(red_score))
    blue_score_total = int(sum(blue_score))
    red_auto_total = int(red_score[0] + red_score[2] +
                         red_score[3] + red_score[5] + red_score[6] + red_score[8])
    blue_auto_total = int(blue_score[
        0] + blue_score[2] + blue_score[3] + blue_score[5] + blue_score[6] + blue_score[8])
    red_teleop_total = int(red_score_total - red_auto_total)
    blue_teleop_total = int(blue_score_total - blue_auto_total)

    red_breach_confirm = red_breach_info[1]
    red_def_one = red_breach_info[2]
    red_def_two = red_breach_info[3]
    red_def_three = red_breach_info[4]
    red_def_four = red_breach_info[5]

    blue_breach_confirm = blue_breach_info[1]
    blue_def_one = blue_breach_info[2]
    blue_def_two = blue_breach_info[3]
    blue_def_three = blue_breach_info[4]
    blue_def_four = blue_breach_info[5]

    winner = ""
    if red_score_total > blue_score_total:
        winner = "RED ALLIANCE WINS"
    else:
        winner = "BLUE ALLIANCE WINS"

    return render(request, 'match-stats.html', {
        'red_score_total': red_score_total,
        'blue_score_total': blue_score_total,
        'red_auto_total': red_auto_total,
        'blue_auto_total': blue_auto_total,
        'red_teleop_total': red_teleop_total,
        'blue_teleop_total': blue_teleop_total,
        'red_breach_confirm': red_breach_confirm,
        'blue_breach_confirm': blue_breach_confirm,
        'red_def_one': red_def_one,
        'red_def_two': red_def_two,
        'red_def_three': red_def_three,
        'red_def_four': red_def_four,
        'blue_def_one': blue_def_one,
        'blue_def_two': blue_def_two,
        'blue_def_three': blue_def_three,
        'blue_def_four': blue_def_four,
        'winner': winner,
        'red_one_number': red_one_number,
        'red_number_two': red_number_two,
        'red_number_three': red_number_three,
        'blue_number_one': blue_number_one,
        'blue_number_two': blue_number_two,
        'blue_number_three': blue_number_three
    }
    )
