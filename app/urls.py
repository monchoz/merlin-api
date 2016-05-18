from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
from . import views

router = routers.DefaultRouter()
router.register(r'task', views.TaskViewSet)

urlpatterns = [
    url(r'^', include(router.urls), name='RestRouter'),
]
