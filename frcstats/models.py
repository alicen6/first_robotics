from django.db import models
from django import forms
from choices import auton_def_choices, teleop_def_choices, defense_options, hang_options
# from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField, GroupedForeignKey


class Event(models.Model):
    event_id = models.IntegerField()
    week_id = models.IntegerField()
    event_name = models.CharField(max_length=50)

    def __unicode__(self):
        return str(self.event_name)

    class Meta:
        db_table = 'events'
        app_label = 'frcstats'


class Team(models.Model):
    team_number = models.IntegerField()
    team_notes = models.CharField(max_length=150)
    event_id = models.ForeignKey(
        'Event', on_delete=models.CASCADE, unique=False)

    def __unicode__(self):
        return str(self.team_number)

    class Meta:
        db_table = 'teams'
        app_label = 'frcstats'


class Match(models.Model):
    team_number = models.ForeignKey(
        'Team', on_delete=models.CASCADE, unique=False)
    match_number = models.IntegerField()
    auton_low_goals = models.IntegerField()
    auton_high_goals = models.IntegerField()
    auton_def_reached = models.CharField(
        max_length=8, choices=auton_def_choices, default=None)
    auton_def_crossed = models.CharField(
        max_length=8, choices=auton_def_choices, default=None)
    teleop_low_goals = models.IntegerField()
    teleop_high_goals = models.IntegerField()
    teleop_portc = models.IntegerField(
        choices=teleop_def_choices, default=None)
    teleop_drawb = models.IntegerField(
        choices=teleop_def_choices, default=None)
    teleop_cdf = models.IntegerField(choices=teleop_def_choices, default=None)
    teleop_moat = models.IntegerField(choices=teleop_def_choices, default=None)
    teleop_sallyp = models.IntegerField(
        choices=teleop_def_choices, default=None)
    teleop_rought = models.IntegerField(
        choices=teleop_def_choices, default=None)
    teleop_lowbar = models.IntegerField(
        choices=teleop_def_choices, default=None)
    teleop_ramparts = models.IntegerField(
        choices=teleop_def_choices, default=None)
    hang_input = models.IntegerField(choices=hang_options, default=None)
    played_def = models.IntegerField(choices=defense_options, default=None)

    class Meta:
        db_table = 'match_info'
        app_label = 'frcstats'
