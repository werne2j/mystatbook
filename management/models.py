from django.db import models

# Create your models here.
class Coach(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

class Team(models.Model):
	coach = models.ForeignKey('Coach')
	year = models.IntegerField(max_length=4)

class Player(models.Model):
	team = models.ForeignKey('Team')
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)


