# encoding:utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
	user = models.IntegerField()
	name = models.CharField(max_length=150)
	start = models.DateTimeField(auto_now_add=False)
	end = models.DateTimeField(auto_now_add=False)
	completed = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name
