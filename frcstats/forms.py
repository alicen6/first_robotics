from django import forms
from .models import Team  # , OtherModelNameHere


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = (
            'team_name', 'team_number', 'robot_weight',
            'robot_height', 'team_location', 'team_notes')
