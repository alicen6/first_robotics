from django.db import models
# from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField, GroupedForeignKey


class Team(models.Model):
    team_number = models.IntegerField()
    team_name = models.CharField(max_length=30)
    robot_weight = models.FloatField()
    robot_height = models.IntegerField()
    team_location = models.CharField(max_length=30)
    team_notes = models.CharField(max_length=150)

    def __unicode__(self):
            return self.team_number

    class Meta:
        db_table = 'teams'
        app_label = 'frcstats'


class Week(models.Model):
    week = models.IntegerField()
    date = models.CharField(max_length=50)

    class Meta:
        db_table = 'weeks'
        app_label = 'frcstats'

class EventName(models.Model):
    event_name = models.CharField(max_length=15)
    event_location = models.CharField(max_length=50)
    week_id = models.ForeignKey(Week)

    class Meta:
        db_table = 'event_name'
        app_label = 'frcstats'

class MatchNumber(models.Model):
    match_number = models.IntegerField()

    class Meta:
        db_table = 'match_number'
        app_label = 'frcstats'

class AutonModel(models.Model):
    auton_high_goals = models.IntegerField()
    auton_low_goals = models.IntegerField()
    auton_def_crossed = models.CharField(max_length=15)
    auton_def_reached = models.CharField(max_length=15)

    class Meta:
        db_table = 'matchstats_auto'
        app_label = 'frcstats'

class TeleopModel(models.Model):
    teleop_high_goals = models.IntegerField()
    teleop_low_goals = models.IntegerField()
    teleop_def_crossed = models.CharField(max_length=15)
    teleop_def_stuck = models.CharField(max_length=15)
    hang_input = models.IntegerField()
    def_played = models.IntegerField()

    class Meta:
        db_table = 'matchstats_teleop'
        app_label = 'frcstats'
