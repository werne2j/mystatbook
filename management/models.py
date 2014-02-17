from django.db import models
from django.contrib.auth.models import User

CLASS_STANDINGS = (('Fr', 'Freshman'), ('So', 'Sophomore'), (
    'Jr', 'Junior'), ('Sr', 'Senior'), ('O', 'Other'))

HAND = (('L', 'Left'), ('R', 'Right'))

# Create your models here.
class Team(models.Model):
	coach = models.OneToOneField(User)
	name = models.CharField(max_length=50)
	year = models.IntegerField(max_length=4)

	def __unicode__(self):
		return unicode(self.name)

class Position(models.Model):
	position = models.CharField(max_length=100)

	def __unicode__(self):
		return self.position

class Player(models.Model):
	team = models.ForeignKey('Team')
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	position = models.ManyToManyField('Position')
	class_standing = models.CharField(max_length=50, choices=CLASS_STANDINGS, blank=True)
	throws = models.CharField(max_length=50, choices=HAND, null=True)
	hits = models.CharField(max_length=50, choices=HAND, null=True)

	def __unicode__(self):
		return u'{first} {last}'.format(first=self.first_name, last=self.last_name)
