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
        return str(int((float(len(stuck)) /
                        (float(len(value)) + float(len(miss)) + float(len(stuck)))) * 100)) + "%"
    else:
        return 0

if len(red_one) > 0 or len(blue_one) > 0:
    red_one_matches = Match.objects.filter(team_number=red_one[0].id)
    red_two_matches = Match.objects.filter(team_number=red_two[0].id)
    red_three_matches = Match.objects.filter(team_number=red_three[0].id)
    blue_one_matches = Match.objects.filter(team_number=blue_one[0].id)
    blue_two_matches = Match.objects.filter(team_number=blue_two[0].id)
    blue_three_matches = Match.objects.filter(team_number=blue_three[0].id)
