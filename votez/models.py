from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class Vote(models.Model):
    reporter = models.ForeignKey('teamMatez.TeamMate',related_name='vote_reporters')
    teamMate = models.ForeignKey('teamMatez.TeamMate',related_name='vote_temmatez')
    weight = models.IntegerField()
    date = models.DateField(default=datetime.date.today())


    def __str__(self):
        return self.reporter.user.username + " voted for " +  self.teamMate.user.username + " " + str(self.date)