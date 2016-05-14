# -*- encoding: utf-8 -*-
from django.core.mail import EmailMessage, EmailMultiAlternatives
from rest_framework import viewsets, generics, mixins, filters
from rest_framework import status
from django.http import HttpResponse, HttpResponseForbidden
from rest_framework.response import Response
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.humanize.templatetags.humanize import naturalday, naturaltime
import django_filters
from .serializers import TaskSerializer
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
	serializer_class = TaskSerializer
	filter_fields = ('user', )
	queryset = Task.objects.all()
