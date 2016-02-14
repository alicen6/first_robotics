from django import forms
from .models import Team as TeamModel
from .models import MatchNumber
from .models import AutonModel
from .models import TeleopModel
from django.forms import ModelForm


class Team(forms.Form):
    team_number = forms.IntegerField(label='Team Number ')
    team_name = forms.CharField(label='Team Name ', max_length=30)


class TeamForm(ModelForm):
    class Meta:
        model = TeamModel
        fields = ['team_number', 'team_name']


class Match(forms.Form):
    match_playing = forms.IntegerField(label='Match Number ')


class MatchForm(ModelForm):
    class Meta:
        model = MatchNumber
        fields = ['match_number']


class Autonomous(forms.Form):
    auton_high_goals = forms.IntegerField(label='How many high goals were scored in autonomous? ')
    auton_low_goals = forms.IntegerField(label='How many low goals were scored in autonomous? ')
    def_choices = (
    ('portc', 'Portcullis'),
    ('cvf', 'Cheval de Frise'),
    ('moat', 'Moat'),
    ('ramparts', 'Ramparts'),
    ('drawb', 'Drawbridge'),
    ('sallyp', 'Sallyport'),
    ('rockwall', 'Rock Wall'),
    ('rought', 'Rough Terrain'),
    ('lowbar', 'Low Bar'),
    ('none', 'None'),
    )
    auton_def_reached = forms.ChoiceField(choices = def_choices, label = 'Which defense was reached in auto? ')
    auton_def_crossed = forms.ChoiceField(choices = def_choices, label = 'Which defense was crossed in auto? ')


class AutonForm(ModelForm):
    class Meta:
        model = AutonModel
        fields = ['auton_high_goals', 'auton_low_goals', 'auton_def_crossed', 'auton_def_reached']


class Teleoperated(forms.Form):
    teleop_high_goals = forms.IntegerField(label='How many high goals were scored in teleop? ')
    teleop_low_goals = forms.IntegerField(label='How many low goals were scored in teleop? ')
    def_choices = (
    ('portc', 'Portcullis'),
    ('cvf', 'Cheval de Frise'),
    ('moat', 'Moat'),
    ('ramparts', 'Ramparts'),
    ('drawb', 'Drawbridge'),
    ('sallyp', 'Sallyport'),
    ('rockwall', 'Rock Wall'),
    ('rought', 'Rough Terrain'),
    ('lowbar', 'Low Bar'),
    ('none', 'None'),
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


class TeleopForm(ModelForm):
    class Meta:
        model = TeleopModel
        fields = ['teleop_high_goals', 'teleop_low_goals', 'teleop_def_crossed', 'teleop_def_stuck', 'hang_input', 'def_played']
