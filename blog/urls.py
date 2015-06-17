# from django.conf.urls import patterns, url
# from django.views.generic import ListView, DetailView
# from blog.models import Post

# urlpatterns = [,
#   url(r'^$', 'blog.views.index'),
#   # Index, with pagination
#   # url(r'^(?P<page>\d+)?/?$', ListView.as_view(
#   #   model = Post,
#   #   paginate_by = 5,
#   #   )),

#   # Individual posts
#   url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/$', 'blog.views.post_detail'),
# ]

from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [
  url(r'^$', 'blog.views.index'),

  # Individual posts
  url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/$', 'blog.views.post_detail'),
]