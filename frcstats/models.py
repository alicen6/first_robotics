from django.db import models
# from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField, GroupedForeignKey


class Team(models.Model):
    team_number = models.IntegerField()
    team_name = models.CharField(max_length=30)
    robot_weight = models.FloatField()
    robot_height = models.IntegerField()
    team_location = models.CharField(max_length=30)
    team_notes = models.CharField(max_length=150)

    posted_on = models.DateTimeField('Posted On')

    def __unicode__(self):
            return self.team_number

    class Meta:
        db_table = 'teams'
        app_label = 'frcstats'


class Week(models.Model):
    week = models.IntegerField()
    date = models.CharField(max_length=50)

class Event_Name(models.Model):
    event_name = models.IntegerField(max_length=50)
    event_location = models.CharField(max_length=50)
    week_id = models.ForeignKey(Week)

# class Event(models.Model):
#    week_id = models.ForeignKey(Week)
#    event_id = GroupedForeignKey(Event_Name, "week_id")
