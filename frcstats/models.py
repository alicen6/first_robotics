from django.db import models


class Team(models.Model):
    team_number = models.IntegerField()
    team_name = models.CharField(max_length=30)
    robot_weight = models.FloatField()
    robot_height = models.IntegerField()
    team_location = models.CharField(max_length=30)
    team_notes = models.CharField(max_length=150)

    class Meta:
        db_table = 'teams'
        app_label = 'frcstats'
