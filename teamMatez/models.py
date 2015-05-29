from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TeamMate(models.Model):
    user = models.ForeignKey(User, unique=True)
    name = models.CharField(max_length=200, blank=True)
    surname = models.CharField(max_length=200, blank=True)
    team = models.ForeignKey('teamz.Team', blank=True)
    isLeader = models.BooleanField(default=False, blank=True)
    avatar = models.ImageField(upload_to='users/avatars/')
    votesNumber = 0


    def __str__(self):
        return self.user.username