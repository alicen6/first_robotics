# FRCstats

This is a web application for tracking information based on the 2016 FIRST FRC game FIRST Stronghold.

## Input Match Info

This is the first available button on the main page of the site. This button takes the user to a scouting page where they can input match information for one robot. The information that is gathered includes:

* match number
* auto high goals
* auto low goals
* auto reaches
* auto crosses
* teleop high goals
* teleop low goals
* teleop crossings
* teleop defense
* hanging

## Lookup Team Stats

This button takes the user to a single input where they can enter a team number. Upon entering a team number, it will display a series of stats and averages based on information input from scouting matches. This page displays the following information:

* team number
* drivetrain
* number of motors
* gear reduction
* notes
* avg auto low goals
* avg auto high goals
* defenses reached in auto
* defenses crossed in auto
* avg teleop high goals
* avg teleop low goals
* avg times a defense is crossed in teleop
* percent of matches stuck on defense
* percent of matches a hang is attempted
* percent of successful hangs
* percent of matches no hang is attempted
* percent of matches defense is played

## Lookup Team Match Info

This button is a lot like the the Team Stats Info button, in that it shows the information from the matches that have been scouted and put into the database. This shows instead the information in a table, by column for each match that was scouted.

## Add Drivetrain Info

This allows the user to input drivetrain (and other) information about an individual team. If a second entry is put into this form for the same team, it will rewrite over the existing entry and update the information. The fields are as follows:

* drivetrain
* number of motors
* gear reduction
* notes

## Compare Two Teams

This button allows for the input of two different team numbers. Once two team numbers are put in, it will display all the same information as Team Stats, but of both teams side by side so that the user can compare. If either team has no information in the database currently, this will not work.

## Lookup Teams By Event

Previously, the only way to see what other events teams that were at your event were going to, was to manually go through things like TBA and write it down for yourself. With this, you can input any event and it will display a table showing all teams at that event and also all other events that those teams are going to.

## Report a Bug or Suggest a Feature

This simply links to the github issues page so that anybody can report it when they find a problem, or if they have an idea for anything they would like to see added to the web application.

## In the Future

In the future, hopefully a feature will be added that allows a user to select 6 teams onto two separate alliances and see the potential outcome of a match between those two alliances.
