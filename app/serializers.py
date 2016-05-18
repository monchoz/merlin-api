# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.humanize.templatetags.humanize import naturalday, naturaltime
from django.shortcuts import get_object_or_404
from .models import Task
from django.core.mail import EmailMultiAlternatives, EmailMessage

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		read_only_fields = ('id', )
