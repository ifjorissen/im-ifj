from blog.models import Post
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
  # get the blog posts that are published
  posts = Post.objects.all
  # now return the rendered template
  return render(request, 'blog/post_list.html', {'object_list': posts})

def post_detail(request, year, month, slug):
  unslug = slug.replace('-', ' ')
  post = Post.objects.get(slug=str(slug))
  return render(request, 'blog/post_detail.html', {'post': post})

def tagged(request, tag):
  posts = Post.objects.filter(tags__slug=tag)
  return render(request, 'blog/post_list.html', {'object_list': posts})
