from django.db import models

# Create your models here.
from django.db.models import ManyToManyField


class Participant(models.Model):
    part_name = models.CharField(max_length=200)
    alive = models.BooleanField(default=1)

    def __unicode__(self):
        return self.part_name

class Week(models.Model):
    participant = models.ForeignKey(Participant)
    team_abbrv = models.CharField(max_length=3)
    week = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.week)
