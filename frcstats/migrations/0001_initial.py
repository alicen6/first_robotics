# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=15)),
                ('event_location', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'event_name',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_number', models.IntegerField()),
                ('auton_high_goals', models.IntegerField()),
                ('auton_low_goals', models.IntegerField()),
                ('auton_def_crossed', models.CharField(max_length=15)),
                ('auton_def_reached', models.CharField(max_length=15)),
                ('teleop_high_goals', models.IntegerField()),
                ('teleop_low_goals', models.IntegerField()),
                ('teleop_def_crossed', models.CharField(max_length=15)),
                ('teleop_def_stuck', models.CharField(max_length=15)),
                ('hang_input', models.IntegerField()),
                ('def_played', models.IntegerField()),
            ],
            options={
                'db_table': 'match_number',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_number', models.IntegerField()),
                ('team_notes', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'teams',
            },
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField()),
                ('date', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'weeks',
            },
        ),
        migrations.AddField(
            model_name='eventname',
            name='week_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frcstats.Week'),
        ),
    ]
