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

class Game(models.Model):
	team = models.ForeignKey('Team')
	date = models.DateField()
	opponent = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	time = models.TimeField()
	doubleheader = models.BooleanField(default=True)

	def __unicode__(self):
		return u'{opp} {d}'.format(opp=self.opponent, d=self.date)

class PlayerStats(models.Model):

	class Meta:
		verbose_name_plural = 'Player Stats'

	game = models.ForeignKey('Game')	
	player = models.ForeignKey('Player', related_name="playerstats")
	at_bats = models.IntegerField(default=0)
	runs = models.IntegerField(default=0)
	hits = models.IntegerField(default=0)
	hr = models.IntegerField(default=0)
	rbi = models.IntegerField(default=0)
	walks = models.IntegerField(default=0)
	strikeouts = models.IntegerField(default=0)
	innings = models.IntegerField(default=0)
	hits_allowed = models.IntegerField(default=0)
	runs_allowed = models.IntegerField(default=0)
	earned_runs = models.IntegerField(default=0)
	walks_allowed = models.IntegerField(default=0)
	strikeout_amount = models.IntegerField(default=0)
	wild_pitches = models.IntegerField(default=0)
	hit_by_pitch = models.IntegerField(default=0)
	win = models.IntegerField(default=0)
	loss = models.IntegerField(default=0)
	sv = models.IntegerField(default=0)

	def __unicode__(self):
		return u'{p} stats'.format(p=self.player)

class DepthChart(models.Model):
	team = models.ForeignKey('Team')
	catch1 = models.CharField(max_length=100, default="Catcher")
	catch2 = models.CharField(max_length=100, default="Catcher")
	first1 = models.CharField(max_length=100, default="First Base")
	first2 = models.CharField(max_length=100, default="First Base")
	second1 = models.CharField(max_length=100, default="Second Base")
	second2 = models.CharField(max_length=100, default="Second Base")
	short1 = models.CharField(max_length=100, default="Shortstop")
	short2 = models.CharField(max_length=100, default="Shortstop")
	third1 = models.CharField(max_length=100, default="Third Base")
	third2 = models.CharField(max_length=100, default="Third Base")
	left1 = models.CharField(max_length=100, default="Left Field")
	left2 = models.CharField(max_length=100, default="Left Field")
	center1 = models.CharField(max_length=100, default="Center Field")
	center2 = models.CharField(max_length=100, default="Center Field")
	right1 = models.CharField(max_length=100, default="Right Field")
	right2 = models.CharField(max_length=100, default="Right Field")
	starter1 = models.CharField(max_length=100, default="Starting Pitcher")
	starter2 = models.CharField(max_length=100, default="Starting Pitcher")
	starter3 = models.CharField(max_length=100, default="Starting Pitcher")
	starter4 = models.CharField(max_length=100, default="Starting Pitcher")
	relief1 = models.CharField(max_length=100, default="Relief Pitcher")
	relief2 = models.CharField(max_length=100, default="Relief Pitcher")
	relief3 = models.CharField(max_length=100, default="Relief Pitcher")
	relief4 = models.CharField(max_length=100, default="Relief Pitcher")
	dh = models.CharField(max_length=100, default="Designated Hitter")

	def __unicode__(self):
		return u'{t} depth chart'.format(t=self.team)


# class IndivPitchStats(models.Model):

# 	class Meta:
# 		verbose_name_plural = 'Individual Pitching Stats'

# 	player = models.ForeignKey('Player')
# 	innings = models.IntegerField(default=0)
# 	hits_allowed = models.IntegerField(default=0)
# 	runs_allowed = models.IntegerField(default=0)
# 	earned_runs = models.IntegerField(default=0)
# 	walks_allowed = models.IntegerField(default=0)
# 	strikeouts = models.IntegerField(default=0)
# 	wild_pitches = models.IntegerField(default=0)
# 	hit_by_pitch = models.IntegerField(default=0)

# 	def __unicode__(self):
# 		return u'{p} pitching stats'.format(p=self.player)



