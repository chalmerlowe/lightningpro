from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Talk(models.Model):
	description = models.CharField(max_length=200)
	priority = models.IntegerField(default=-2)
	name = models.CharField(max_length=100, null=True)
	email = models.EmailField(max_length=100, null=True)
	def __str__(self):
		return self.description



