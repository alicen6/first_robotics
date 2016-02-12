from django import forms


class Team(forms.Form):
    team_number = forms.IntegerField(label='Team Number ')
    team_name = forms.CharField(label='Team Name ', max_length=30)


class Match(forms.Form):
    match_playing = forms.IntegerField(label='Match Number ')


class Autonomous(forms.Form):
    auton_high_goals = forms.IntegerField(label='How many high goals were scored in autonomous? ')
    auton_low_goals = forms.IntegerField(label='How many low goals were scored in autonomous? ')
    def_choices = (
    ('Portcullis', 'Portcullis'),
    ('Cheval de Frise', 'Cheval de Frise'),
    ('Moat', 'Moat'),
    ('Ramparts', 'Ramparts'),
    ('Drawbridge', 'Drawbridge'),
    ('Sallyport', 'Sallyport'),
    ('Rock Wall', 'Rock Wall'),
    ('Rough Terrain', 'Rough Terrain'),
    ('Low Bar', 'Low Bar'),
    ('None', 'None'),
    )
    auton_def_reached = forms.ChoiceField(choices = def_choices, label = 'Which defense was reached in auto? ')
    auton_def_crossed = forms.ChoiceField(choices = def_choices, label = 'Which defense was crossed in auto? ')


class Teleoperated(forms.Form):
    teleop_high_goals = forms.IntegerField(label='How many high goals were scored in teleop? ')
    teleop_low_goals = forms.IntegerField(label='How many low goals were scored in teleop? ')
    def_choices = (
    ('Portcullis', 'Portcullis'),
    ('Cheval de Frise', 'Cheval de Frise'),
    ('Moat', 'Moat'),
    ('Ramparts', 'Ramparts'),
    ('Drawbridge', 'Drawbridge'),
    ('Sallyport', 'Sallyport'),
    ('Rock Wall', 'Rock Wall'),
    ('Rough Terrain', 'Rough Terrain'),
    ('Low Bar', 'Low Bar'),
    ('None', 'None'),
    )
    teleop_def_crossed = forms.MultipleChoiceField(choices = def_choices, label = "Which defenses were crossed? ")
    teleop_def_stuck = forms.MultipleChoiceField(choices = def_choices, label = "Did the robot get stuck? ")
    hang_choices = (
    ('0', 'Did not hang'),
    ('1', 'Attempted to hang'),
    ('2', 'Successful hang'),
    )
    hang_input = forms.ChoiceField(choices = hang_choices, label = "Did the robot hang? ")
    yes_or_no = (
    ('0', 'no'),
    ('1', 'yes'),
    )
    def_played = forms.ChoiceField(choices = yes_or_no, label = "Did the robot play defense? ")
