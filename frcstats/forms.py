from django import forms
from .models import Team, Match # , OtherModelNameHere


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = '__all__'
