# from django.shortcuts import render


# def index(request):
# 	# get the blog posts that are published
# 	projects = Project.objects.all
# 	# now return the rendered template
# 	return render(request, 'playground/index.html', {'object_list': projects})


from playground.models import Project
from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
	# get the blog posts that are published
	projects = Project.objects.all
	# now return the rendered template
	return render(request, 'playground/project_list.html', {'project_list': projects})

def project_detail(request, slug):
	project = Project.objects.get(slug=str(slug))
	return render(request, 'playground/project_detail.html', {'project': project})