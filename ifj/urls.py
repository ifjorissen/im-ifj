"""ifj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #django app urls
    url(r'^blog/', include('blog.urls')),
    url(r'^playground/', include('playground.urls')),
    #static pages urls
    url(r'^about-me/', 
      TemplateView.as_view(template_name='pages/about.html'),
      name='about-me'),
    url(r'^find-me/', 
      TemplateView.as_view(template_name='pages/find-me.html'),
      name='find-me'),
    url(r'^resu-me/', 
      TemplateView.as_view(template_name='pages/resume.html'),
      name='resu-me'),
    url(r'^$', 
      TemplateView.as_view(template_name='pages/about.html'),
      name='landing'),
]

# from django.conf.urls import patterns, include, url
# from django.contrib import admin
# from staticpages.views import HomeView, AboutView, FindMeView, ResumeView

# admin.autodiscover()

# urlpatterns = patterns('',

#   #admin urls
#   url(r'^admin/', include(admin.site.urls)),

#   #photography gallery urls
#   url(r'^photography/', include('photography.urls')),
#   # url(r'^photologue/', include('photologue.urls', namespace='photologue')),

#   #django app urls
#   url(r'^blog/', include('blogengine.urls')),
#   url(r'^playground/', include('playground.urls')),

#   #static pages urls
#   url(r'^about-me/', AboutView.as_view()),
#   url(r'^find-me/', FindMeView.as_view()),
#   url(r'^resume/', ResumeView.as_view()),
#   url(r'^$', AboutView.as_view())
#   # url(r'^$', HomeView.as_view())
  
# )

  # url(r'^about-me/', 
 #    TemplateView.as_view(template_name='templates/about.html'),
 #    name='about-me'),
  # url(r'^find-me/', 
 #    TemplateView.as_view(template_name='templates/find-me.html'),
 #    name='find-me'),
 #  url(r'^resu-me/', 
 #    TemplateView.as_view(template_name='templates/resume.html'),
 #    name='resu-me'),
