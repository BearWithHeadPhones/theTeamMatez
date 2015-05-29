from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.


class LevelOfAppreciation(models.Model):
    description = models.CharField(max_length=30)
    icon = models.ImageField(upload_to='levelofappreciation/icons/')
    weight = models.IntegerField(default=1, blank=True)

    def __str__(self):
        return self.description


class Vote(models.Model):
    reporter = models.ForeignKey('teamMatez.TeamMate',related_name='vote_reporters')
    teamMate = models.ForeignKey('teamMatez.TeamMate',related_name='vote_temmatez')
    levelOfAppreciation = models.ForeignKey(LevelOfAppreciation)
    wordsOfAppreciation = models.CharField(max_length=200)
    date = models.DateField(default=datetime.date.today())


    def __str__(self):
        return self.reporter.user.username + " appreciated " +  self.teamMate.user.username + " " + str(self.date)


