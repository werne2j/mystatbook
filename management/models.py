from django.db import models

# Create your models here.
class Coach(models.Model):
	first_name = models.CharField(max_length=True)
	last_name = models.CharField(max_length=True)
	email = models.EmailField()
