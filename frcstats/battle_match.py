red= Team.objects.filter(team_number=red_one)
red_two = Team.objects.filter(team_number=red_two)
red_three = Team.objects.filter(team_number=red_three)

blue= Team.objects.filter(team_number=blue_one)
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

if len(red) > 0 or len(blue) > 0:
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
red_one_portc_stats_value= defense_cross(
    red_one_portc_stats, red_one_portc_miss_stats)
red_one_portc_stuck_stats= defense_stuck(
    red_one_portc_stats, red_one_portc_miss_stats, red_one_portc_stuck_stats)
red_one_drawb_stats_value= defense_cross(
    red_one_drawb_stats, red_one_drawb_miss_stats)
red_one_drawb_stuck_stats= defense_stuck(
    red_one_drawb_stats, red_one_drawb_miss_stats, red_one_drawb_stuck_stats)
red_one_cdf_stats_value= defense_cross(red_one_cdf_stats, red_one_cdf_miss_stats)
red_one_cdf_stuck_stats= defense_stuck(
    red_one_cdf_stats, red_one_cdf_miss_stats, red_one_cdf_stuck_stats)
red_one_moat_stats_value= defense_cross(
    red_one_moat_stats, red_one_moat_miss_stats)
red_one_moat_stuck_stats= defense_stuck(
    red_one_moat_stats, red_one_moat_miss_stats, red_one_moat_stuck_stats)
red_one_sallyp_stats_value= defense_cross(
    red_one_sallyp_stats, red_one_sallyp_miss_stats)
red_one_sallyp_stuck_stats= defense_stuck(
    red_one_sallyp_stats, red_one_sallyp_miss_stats, red_one_sallyp_stuck_stats)
red_one_rought_stats_value= defense_cross(
    red_one_rought_stats, red_one_rought_miss_stats)
red_one_rought_stuck_stats= defense_stuck(
    red_one_rought_stats, red_one_rought_miss_stats, red_one_rought_stuck_stats)
red_one_lowbar_stats_value= defense_cross(
    red_one_lowbar_stats, red_one_lowbar_miss_stats)
red_one_lowbar_stuck_stats= defense_stuck(
    red_one_lowbar_stats, red_one_lowbar_miss_stats, red_one_lowbar_stuck_stats)
red_one_ramparts_stats_value= defense_cross(
    red_one_ramparts_stats, red_one_ramparts_miss_stats)
red_one_ramparts_stuck_stats= defense_stuck(
    red_one_ramparts_stats, red_one_ramparts_miss_stats, red_one_ramparts_stuck_stats)
red_one_rockwall_stats_value= defense_cross(
    red_one_rockwall_stats, red_one_rockwall_miss_stats)
red_one_rockwall_stuck_stats= defense_stuck(
    red_one_rockwall_stats, red_one_rockwall_miss_stats, red_one_rockwall_stuck_stats)
red_one_hang_success_stats= hang_succes(
    red_one_hang_input_values, red_one_hang_success_values)
red_one_played_def_stats= played_def(red_one_played_def_values)
red_one_hang_value= hang_total(
    red_one_hang_input_values, red_one_hang_success_values, red_one_hang_fail_values)
red_one_hang_fail= hang_fail(red_one_hang_input_values, red_one_hang_fail_values)
red_one_auton_low_stats= auto_lows(red_one_auton_low_values)
red_one_auton_high_stats= auto_highs(red_one_auton_high_values)
red_one_teleop_low_stats= teleop_lows(red_one_teleop_low_values)
red_one_teleop_high_stats= teleop_highs(red_one_teleop_high_values)

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
red_two_portc_stats_value= defense_cross(
    red_two_portc_stats, red_two_portc_miss_stats)
red_two_portc_stuck_stats= defense_stuck(
    red_two_portc_stats, red_two_portc_miss_stats, red_two_portc_stuck_stats)
red_two_drawb_stats_value= defense_cross(
    red_two_drawb_stats, red_two_drawb_miss_stats)
red_two_drawb_stuck_stats= defense_stuck(
    red_two_drawb_stats, red_two_drawb_miss_stats, red_two_drawb_stuck_stats)
red_two_cdf_stats_value= defense_cross(red_two_cdf_stats, red_two_cdf_miss_stats)
red_two_cdf_stuck_stats= defense_stuck(
    red_two_cdf_stats, red_two_cdf_miss_stats, red_two_cdf_stuck_stats)
red_two_moat_stats_value= defense_cross(
    red_two_moat_stats, red_two_moat_miss_stats)
red_two_moat_stuck_stats= defense_stuck(
    red_two_moat_stats, red_two_moat_miss_stats, red_two_moat_stuck_stats)
red_two_sallyp_stats_value= defense_cross(
    red_two_sallyp_stats, red_two_sallyp_miss_stats)
red_two_sallyp_stuck_stats= defense_stuck(
    red_two_sallyp_stats, red_two_sallyp_miss_stats, red_two_sallyp_stuck_stats)
red_two_rought_stats_value= defense_cross(
    red_two_rought_stats, red_two_rought_miss_stats)
red_two_rought_stuck_stats= defense_stuck(
    red_two_rought_stats, red_two_rought_miss_stats, red_two_rought_stuck_stats)
red_two_lowbar_stats_value= defense_cross(
    red_two_lowbar_stats, red_two_lowbar_miss_stats)
red_two_lowbar_stuck_stats= defense_stuck(
    red_two_lowbar_stats, red_two_lowbar_miss_stats, red_two_lowbar_stuck_stats)
red_two_ramparts_stats_value= defense_cross(
    red_two_ramparts_stats, red_two_ramparts_miss_stats)
red_two_ramparts_stuck_stats= defense_stuck(
    red_two_ramparts_stats, red_two_ramparts_miss_stats, red_two_ramparts_stuck_stats)
red_two_rockwall_stats_value= defense_cross(
    red_two_rockwall_stats, red_two_rockwall_miss_stats)
red_two_rockwall_stuck_stats= defense_stuck(
    red_two_rockwall_stats, red_two_rockwall_miss_stats, red_two_rockwall_stuck_stats)
red_two_hang_success_stats= hang_succes(
    red_two_hang_input_values, red_two_hang_success_values)
red_two_played_def_stats= played_def(red_two_played_def_values)
red_two_hang_value= hang_total(
    red_two_hang_input_values, red_two_hang_success_values, red_two_hang_fail_values)
red_two_hang_fail= hang_fail(red_two_hang_input_values, red_two_hang_fail_values)
red_two_auton_low_stats= auto_lows(red_two_auton_low_values)
red_two_auton_high_stats= auto_highs(red_two_auton_high_values)
red_two_teleop_low_stats= teleop_lows(red_two_teleop_low_values)
red_two_teleop_high_stats= teleop_highs(red_two_teleop_high_values)

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
red_three_portc_stats_value= defense_cross(
    red_three_portc_stats, red_three_portc_miss_stats)
red_three_portc_stuck_stats= defense_stuck(
    red_three_portc_stats, red_three_portc_miss_stats, red_three_portc_stuck_stats)
red_three_drawb_stats_value= defense_cross(
    red_three_drawb_stats, red_three_drawb_miss_stats)
red_three_drawb_stuck_stats= defense_stuck(
    red_three_drawb_stats, red_three_drawb_miss_stats, red_three_drawb_stuck_stats)
red_three_cdf_stats_value= defense_cross(red_three_cdf_stats, red_three_cdf_miss_stats)
red_three_cdf_stuck_stats= defense_stuck(
    red_three_cdf_stats, red_three_cdf_miss_stats, red_three_cdf_stuck_stats)
red_three_moat_stats_value= defense_cross(
    red_three_moat_stats, red_three_moat_miss_stats)
red_three_moat_stuck_stats= defense_stuck(
    red_three_moat_stats, red_three_moat_miss_stats, red_three_moat_stuck_stats)
red_three_sallyp_stats_value= defense_cross(
    red_three_sallyp_stats, red_three_sallyp_miss_stats)
red_three_sallyp_stuck_stats= defense_stuck(
    red_three_sallyp_stats, red_three_sallyp_miss_stats, red_three_sallyp_stuck_stats)
red_three_rought_stats_value= defense_cross(
    red_three_rought_stats, red_three_rought_miss_stats)
red_three_rought_stuck_stats= defense_stuck(
    red_three_rought_stats, red_three_rought_miss_stats, red_three_rought_stuck_stats)
red_three_lowbar_stats_value= defense_cross(
    red_three_lowbar_stats, red_three_lowbar_miss_stats)
red_three_lowbar_stuck_stats= defense_stuck(
    red_three_lowbar_stats, red_three_lowbar_miss_stats, red_three_lowbar_stuck_stats)
red_three_ramparts_stats_value= defense_cross(
    red_three_ramparts_stats, red_three_ramparts_miss_stats)
red_three_ramparts_stuck_stats= defense_stuck(
    red_three_ramparts_stats, red_three_ramparts_miss_stats, red_three_ramparts_stuck_stats)
red_three_rockwall_stats_value= defense_cross(
    red_three_rockwall_stats, red_three_rockwall_miss_stats)
red_three_rockwall_stuck_stats= defense_stuck(
    red_three_rockwall_stats, red_three_rockwall_miss_stats, red_three_rockwall_stuck_stats)
red_three_hang_success_stats= hang_succes(
    red_three_hang_input_values, red_three_hang_success_values)
red_three_played_def_stats= played_def(red_three_played_def_values)
red_three_hang_value= hang_total(
    red_three_hang_input_values, red_three_hang_success_values, red_three_hang_fail_values)
red_three_hang_fail= hang_fail(red_three_hang_input_values, red_three_hang_fail_values)
red_three_auton_low_stats= auto_lows(red_three_auton_low_values)
red_three_auton_high_stats= auto_highs(red_three_auton_high_values)
red_three_teleop_low_stats= teleop_lows(red_three_teleop_low_values)
red_three_teleop_high_stats= teleop_highs(red_three_teleop_high_values)

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
blue_one_portc_stats_value= defense_cross(
    blue_one_portc_stats, blue_one_portc_miss_stats)
blue_one_portc_stuck_stats= defense_stuck(
    blue_one_portc_stats, blue_one_portc_miss_stats, blue_one_portc_stuck_stats)
blue_one_drawb_stats_value= defense_cross(
    blue_one_drawb_stats, blue_one_drawb_miss_stats)
blue_one_drawb_stuck_stats= defense_stuck(
    blue_one_drawb_stats, blue_one_drawb_miss_stats, blue_one_drawb_stuck_stats)
blue_one_cdf_stats_value= defense_cross(blue_one_cdf_stats, blue_one_cdf_miss_stats)
blue_one_cdf_stuck_stats= defense_stuck(
    blue_one_cdf_stats, blue_one_cdf_miss_stats, blue_one_cdf_stuck_stats)
blue_one_moat_stats_value= defense_cross(
    blue_one_moat_stats, blue_one_moat_miss_stats)
blue_one_moat_stuck_stats= defense_stuck(
    blue_one_moat_stats, blue_one_moat_miss_stats, blue_one_moat_stuck_stats)
blue_one_sallyp_stats_value= defense_cross(
    blue_one_sallyp_stats, blue_one_sallyp_miss_stats)
blue_one_sallyp_stuck_stats= defense_stuck(
    blue_one_sallyp_stats, blue_one_sallyp_miss_stats, blue_one_sallyp_stuck_stats)
blue_one_rought_stats_value= defense_cross(
    blue_one_rought_stats, blue_one_rought_miss_stats)
blue_one_rought_stuck_stats= defense_stuck(
    blue_one_rought_stats, blue_one_rought_miss_stats, blue_one_rought_stuck_stats)
blue_one_lowbar_stats_value= defense_cross(
    blue_one_lowbar_stats, blue_one_lowbar_miss_stats)
blue_one_lowbar_stuck_stats= defense_stuck(
    blue_one_lowbar_stats, blue_one_lowbar_miss_stats, blue_one_lowbar_stuck_stats)
blue_one_ramparts_stats_value= defense_cross(
    blue_one_ramparts_stats, blue_one_ramparts_miss_stats)
blue_one_ramparts_stuck_stats= defense_stuck(
    blue_one_ramparts_stats, blue_one_ramparts_miss_stats, blue_one_ramparts_stuck_stats)
blue_one_rockwall_stats_value= defense_cross(
    blue_one_rockwall_stats, blue_one_rockwall_miss_stats)
blue_one_rockwall_stuck_stats= defense_stuck(
    blue_one_rockwall_stats, blue_one_rockwall_miss_stats, blue_one_rockwall_stuck_stats)
blue_one_hang_success_stats= hang_succes(
    blue_one_hang_input_values, blue_one_hang_success_values)
blue_one_played_def_stats= played_def(blue_one_played_def_values)
blue_one_hang_value= hang_total(
    blue_one_hang_input_values, blue_one_hang_success_values, blue_one_hang_fail_values)
blue_one_hang_fail= hang_fail(blue_one_hang_input_values, blue_one_hang_fail_values)
blue_one_auton_low_stats= auto_lows(blue_one_auton_low_values)
blue_one_auton_high_stats= auto_highs(blue_one_auton_high_values)
blue_one_teleop_low_stats= teleop_lows(blue_one_teleop_low_values)
blue_one_teleop_high_stats= teleop_highs(blue_one_teleop_high_values)

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
blue_two_portc_stats_value= defense_cross(
    blue_two_portc_stats, blue_two_portc_miss_stats)
blue_two_portc_stuck_stats= defense_stuck(
    blue_two_portc_stats, blue_two_portc_miss_stats, blue_two_portc_stuck_stats)
blue_two_drawb_stats_value= defense_cross(
    blue_two_drawb_stats, blue_two_drawb_miss_stats)
blue_two_drawb_stuck_stats= defense_stuck(
    blue_two_drawb_stats, blue_two_drawb_miss_stats, blue_two_drawb_stuck_stats)
blue_two_cdf_stats_value= defense_cross(blue_two_cdf_stats, blue_two_cdf_miss_stats)
blue_two_cdf_stuck_stats= defense_stuck(
    blue_two_cdf_stats, blue_two_cdf_miss_stats, blue_two_cdf_stuck_stats)
blue_two_moat_stats_value= defense_cross(
    blue_two_moat_stats, blue_two_moat_miss_stats)
blue_two_moat_stuck_stats= defense_stuck(
    blue_two_moat_stats, blue_two_moat_miss_stats, blue_two_moat_stuck_stats)
blue_two_sallyp_stats_value= defense_cross(
    blue_two_sallyp_stats, blue_two_sallyp_miss_stats)
blue_two_sallyp_stuck_stats= defense_stuck(
    blue_two_sallyp_stats, blue_two_sallyp_miss_stats, blue_two_sallyp_stuck_stats)
blue_two_rought_stats_value= defense_cross(
    blue_two_rought_stats, blue_two_rought_miss_stats)
blue_two_rought_stuck_stats= defense_stuck(
    blue_two_rought_stats, blue_two_rought_miss_stats, blue_two_rought_stuck_stats)
blue_two_lowbar_stats_value= defense_cross(
    blue_two_lowbar_stats, blue_two_lowbar_miss_stats)
blue_two_lowbar_stuck_stats= defense_stuck(
    blue_two_lowbar_stats, blue_two_lowbar_miss_stats, blue_two_lowbar_stuck_stats)
blue_two_ramparts_stats_value= defense_cross(
    blue_two_ramparts_stats, blue_two_ramparts_miss_stats)
blue_two_ramparts_stuck_stats= defense_stuck(
    blue_two_ramparts_stats, blue_two_ramparts_miss_stats, blue_two_ramparts_stuck_stats)
blue_two_rockwall_stats_value= defense_cross(
    blue_two_rockwall_stats, blue_two_rockwall_miss_stats)
blue_two_rockwall_stuck_stats= defense_stuck(
    blue_two_rockwall_stats, blue_two_rockwall_miss_stats, blue_two_rockwall_stuck_stats)
blue_two_hang_success_stats= hang_succes(
    blue_two_hang_input_values, blue_two_hang_success_values)
blue_two_played_def_stats= played_def(blue_two_played_def_values)
blue_two_hang_value= hang_total(
    blue_two_hang_input_values, blue_two_hang_success_values, blue_two_hang_fail_values)
blue_two_hang_fail= hang_fail(blue_two_hang_input_values, blue_two_hang_fail_values)
blue_two_auton_low_stats= auto_lows(blue_two_auton_low_values)
blue_two_auton_high_stats= auto_highs(blue_two_auton_high_values)
blue_two_teleop_low_stats= teleop_lows(blue_two_teleop_low_values)
blue_two_teleop_high_stats= teleop_highs(blue_two_teleop_high_values)

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
blue_three_portc_stats_value= defense_cross(
    blue_three_portc_stats, blue_three_portc_miss_stats)
blue_three_portc_stuck_stats= defense_stuck(
    blue_three_portc_stats, blue_three_portc_miss_stats, blue_three_portc_stuck_stats)
blue_three_drawb_stats_value= defense_cross(
    blue_three_drawb_stats, blue_three_drawb_miss_stats)
blue_three_drawb_stuck_stats= defense_stuck(
    blue_three_drawb_stats, blue_three_drawb_miss_stats, blue_three_drawb_stuck_stats)
blue_three_cdf_stats_value= defense_cross(blue_three_cdf_stats, blue_three_cdf_miss_stats)
blue_three_cdf_stuck_stats= defense_stuck(
    blue_three_cdf_stats, blue_three_cdf_miss_stats, blue_three_cdf_stuck_stats)
blue_three_moat_stats_value= defense_cross(
    blue_three_moat_stats, blue_three_moat_miss_stats)
blue_three_moat_stuck_stats= defense_stuck(
    blue_three_moat_stats, blue_three_moat_miss_stats, blue_three_moat_stuck_stats)
blue_three_sallyp_stats_value= defense_cross(
    blue_three_sallyp_stats, blue_three_sallyp_miss_stats)
blue_three_sallyp_stuck_stats= defense_stuck(
    blue_three_sallyp_stats, blue_three_sallyp_miss_stats, blue_three_sallyp_stuck_stats)
blue_three_rought_stats_value= defense_cross(
    blue_three_rought_stats, blue_three_rought_miss_stats)
blue_three_rought_stuck_stats= defense_stuck(
    blue_three_rought_stats, blue_three_rought_miss_stats, blue_three_rought_stuck_stats)
blue_three_lowbar_stats_value= defense_cross(
    blue_three_lowbar_stats, blue_three_lowbar_miss_stats)
blue_three_lowbar_stuck_stats= defense_stuck(
    blue_three_lowbar_stats, blue_three_lowbar_miss_stats, blue_three_lowbar_stuck_stats)
blue_three_ramparts_stats_value= defense_cross(
    blue_three_ramparts_stats, blue_three_ramparts_miss_stats)
blue_three_ramparts_stuck_stats= defense_stuck(
    blue_three_ramparts_stats, blue_three_ramparts_miss_stats, blue_three_ramparts_stuck_stats)
blue_three_rockwall_stats_value= defense_cross(
    blue_three_rockwall_stats, blue_three_rockwall_miss_stats)
blue_three_rockwall_stuck_stats= defense_stuck(
    blue_three_rockwall_stats, blue_three_rockwall_miss_stats, blue_three_rockwall_stuck_stats)
blue_three_hang_success_stats= hang_succes(
    blue_three_hang_input_values, blue_three_hang_success_values)
blue_three_played_def_stats= played_def(blue_three_played_def_values)
blue_three_hang_value= hang_total(
    blue_three_hang_input_values, blue_three_hang_success_values, blue_three_hang_fail_values)
blue_three_hang_fail= hang_fail(blue_three_hang_input_values, blue_three_hang_fail_values)
blue_three_auton_low_stats= auto_lows(blue_three_auton_low_values)
blue_three_auton_high_stats= auto_highs(blue_three_auton_high_values)
blue_three_teleop_low_stats= teleop_lows(blue_three_teleop_low_values)
blue_three_teleop_high_stats= teleop_highs(blue_three_teleop_high_values)


# next step is to develop actual scores from data about teams
