from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from playground.models import Project

urlpatterns = [
	url(r'^$', 'playground.views.index'),

	# Individual posts
	url(r'^(?P<slug>[a-zA-Z0-9-]+)/?$', 'playground.views.project_detail'),
]