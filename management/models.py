from django.db import models
from fractions import Fraction
from django.contrib.auth.models import User
from django.db.models import Sum, Count
from django.templatetags.static import static
from PIL import Image

CLASS_STANDINGS = (('Fr', 'Freshman'), ('So', 'Sophomore'), (
    'Jr', 'Junior'), ('Sr', 'Senior'), ('O', 'Other'))

HAND = (('L', 'Left'), ('R', 'Right'))

INNINGS = ((0, 0), (1, 1), (2, 2))

# Create your models here.
class Team(models.Model):
	coach = models.ForeignKey(User)
	name = models.CharField(max_length=50)
	logo = models.ImageField(upload_to='logos/', blank=True, null=True)

	def __unicode__(self):
		return unicode(self.name)

	def latest_year(self):
		return self.season_set.all().order_by("-year")[0]

	def get_logo(self):
		if not self.logo:
			return static('baseball.png')
		return self.logo.url

class Season(models.Model):
	team = models.ForeignKey('Team')
	year = models.IntegerField(max_length=4)
	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'{n} {y}'.format(n=self.team.name, y=self.year)

class Position(models.Model):
	position = models.CharField(max_length=100)

	def __unicode__(self):
		return self.position

class Player(models.Model):
	season = models.ForeignKey('Season', null=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	position = models.ManyToManyField('Position')
	class_standing = models.CharField(max_length=50, choices=CLASS_STANDINGS, blank=True)
	throws = models.CharField(max_length=50, choices=HAND, null=True)
	hits = models.CharField(max_length=50, choices=HAND, null=True)

	def __unicode__(self):
		return u'{first} {last}'.format(first=self.first_name, last=self.last_name)

	def hit_totals(self):
		return HitterStats.objects.filter(player=self).aggregate(Count("game"), Sum("at_bats"),
			Sum("runs"), Sum("hits"), Sum("doubles"), Sum("triples"), Sum("hr"), Sum("rbi"),
			Sum("walks"),Sum("hbp"),Sum("sacrafice"),Sum("strikeouts"))

	def pitch_totals(self):
		return PitcherStats.objects.filter(player=self).aggregate(Count("game"), Count("starting_pitcher"), Sum("full_innings"),
			Sum("hits_allowed"), Sum("runs_allowed"), Sum("earned_runs"), Sum("walks_allowed"), Sum("strikeout_amount"), Sum("wild_pitches"),
			Sum("hit_by_pitch"),Sum("win"),Sum("loss"),Sum("sv"))


	def innings(self):
		i = PitcherStats.objects.filter(player=self).aggregate(Sum("full_innings"))
		fi = float(i.values()[0])
		p = PitcherStats.objects.filter(player=self).aggregate(Sum("part_innings"))
		pi = float(p.values()[0])

		ti = int(((fi*3) + pi) / 3)
		ri = int(((fi*3) + pi) % 3)

		return str(ti) + "." + str(ri)

	def plate_apperances(self):
		a = HitterStats.objects.filter(player=self).aggregate(Sum("at_bats"))
		ab = a.values()[0] or 0
		w = HitterStats.objects.filter(player=self).aggregate(Sum("walks"))
		bb = w.values()[0] or 0
		h = HitterStats.objects.filter(player=self).aggregate(Sum("hbp"))
		hp = h.values()[0] or 0
		s = HitterStats.objects.filter(player=self).aggregate(Sum("sacrafice"))
		sf = s.values()[0] or 0

		pa = ab + bb + hp + sf

		return pa

	def average(self):
		b = HitterStats.objects.filter(player=self).aggregate(Sum("at_bats"))
		a =  float(b.values()[0])
		f = HitterStats.objects.filter(player=self).aggregate(Sum("hits"))
		h =  float(f.values()[0])
		avg = h/a
		average = ("%.3f" % avg)
		return average

	def on_base(self):
		a = HitterStats.objects.filter(player=self).aggregate(Sum("hits"))
		h = float(a.values()[0])
		b = HitterStats.objects.filter(player=self).aggregate(Sum("walks"))
		bb = float(b.values()[0])
		c = HitterStats.objects.filter(player=self).aggregate(Sum("hbp"))
		hbp = float(c.values()[0])
		d = HitterStats.objects.filter(player=self).aggregate(Sum("at_bats"))
		ab = float(d.values()[0])
		e = HitterStats.objects.filter(player=self).aggregate(Sum("sacrafice"))
		sf = float(e.values()[0])

		t = h+bb+hbp
		b = ab+bb+hbp+sf
		o = t/b
		obp = ("%.3f" % o)

		return obp

	def slug(self):
		ab = HitterStats.objects.filter(player=self).aggregate(Sum("at_bats"))
		a = float(ab.values()[0])
		hits = HitterStats.objects.filter(player=self).aggregate(Sum("hits"))
		h = float(hits.values()[0])
		doub = HitterStats.objects.filter(player=self).aggregate(Sum("doubles"))
		d = float(doub.values()[0])
		trip = HitterStats.objects.filter(player=self).aggregate(Sum("triples"))
		t = float(trip.values()[0])
		homerun = HitterStats.objects.filter(player=self).aggregate(Sum("hr"))
		hr = float(homerun.values()[0])

		s = h - (d+t+hr)
		top = s + (2*d) + (3*t) + (4*hr)
		slg = top/a
		slgp = ("%.3f" % slg)

		return slgp

	def era(self):
		i = PitcherStats.objects.filter(player=self).aggregate(Sum("full_innings"))
		ip = float(i.values()[0]) or 0
		r = PitcherStats.objects.filter(player=self).aggregate(Sum("earned_runs"))
		er = float(r.values()[0]) or 0

		era = (er / ip) * 9
		return ("%.2f" % era)


class Game(models.Model):
	season = models.ForeignKey('Season', null=True)
	date = models.DateField()
	opponent = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	time = models.TimeField()
	doubleheader = models.BooleanField(default=False)
	conference = models.BooleanField(default=False)

	def __unicode__(self):
		return u'{opp} {d} {t}'.format(opp=self.opponent, d=self.date, t=self.time)

class HitterStats(models.Model):

	class Meta:
		verbose_name_plural = 'Hitting Stats'

	game = models.ForeignKey('Game')
	player = models.ForeignKey('Player', related_name="hitstats")
	at_bats = models.IntegerField(default=0)
	runs = models.IntegerField(default=0)
	hits = models.IntegerField(default=0)
	doubles = models.IntegerField(default=0)
	triples = models.IntegerField(default=0)
	hr = models.IntegerField(default=0)
	rbi = models.IntegerField(default=0)
	walks = models.IntegerField(default=0)
	hbp = models.IntegerField(default=0)
	sacrafice = models.IntegerField(default=0)
	strikeouts = models.IntegerField(default=0)


	def __unicode__(self):
		return u'{p} hitting stats'.format(p=self.player)

class PitcherStats(models.Model):

	class Meta:
		verbose_name_plural = 'Pitching Stats'

	game = models.ForeignKey('Game')
	player = models.ForeignKey('Player', related_name="pitchstats")
	starting_pitcher = models.BooleanField(default=False)
	full_innings = models.IntegerField(default=0)
	part_innings = models.IntegerField(choices=INNINGS, default=0)
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
		return u'{p} pitching stats'.format(p=self.player)


class DepthChart(models.Model):
	season = models.ForeignKey('Season', null=True)
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
		return u'{t} depth chart'.format(t=self.season)

