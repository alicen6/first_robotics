from django import forms
from .models import Team, Match  # , OtherModelNameHere


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = '__all__'


class MatchForm(forms.ModelForm):
    auton_low_goals = forms.IntegerField(label="Autonomous Low Goals Scored")
    auton_high_goals = forms.IntegerField(label="Autonomous High Goals Scored")
    teleop_low_goals = forms.IntegerField(
        label="Teleoperated Low Goals Scored")
    teleop_high_goals = forms.IntegerField(
        label="Teleoperated High Goals Scored")

    class Meta:
        model = Match
        fields = '__all__'
        widgets = {
            'auton_def_reached': forms.RadioSelect,
            'auton_def_crossed': forms.RadioSelect,
            'teleop_portc': forms.RadioSelect,
            'teleop_cdf': forms.RadioSelect,
            'teleop_moat': forms.RadioSelect,
            'teleop_ramparts': forms.RadioSelect,
            'teleop_drawb': forms.RadioSelect,
            'teleop_sallyp': forms.RadioSelect,
            'teleop_rockwall': forms.RadioSelect,
            'teleop_rought': forms.RadioSelect,
            'teleop_lowbar': forms.RadioSelect,
            'hang_input': forms.RadioSelect,
            'played_def': forms.RadioSelect
        }
