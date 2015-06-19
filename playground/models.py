
# Create your models here.
from django.db import models

# Create your models here.

def thumbnail_image_path(instance, filename):
  # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
  return 'playground/project_{0}/thumbnail/{1}'.format(instance.slug, filename)

def image_path(instance, filename):
  # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
  return 'playground/project_{0}/screenshots/{1}'.format(instance.proj.slug, filename)

class ProjectImage(models.Model):
  proj = models.ForeignKey('Project', null=True)
  caption = models.TextField()
  projimg = models.ImageField(upload_to=image_path, null=True) #ideally also include project name

  # def __str__(self):
  #   return self.url

class Project(models.Model):
  #to do: multiple image uploads
  title = models.CharField(max_length = 200)
  pub_date = models.DateTimeField('date added to site')
  projurl = models.URLField()
  completion_date = models.DateTimeField('date completed')
  # thumbnail = models.ForeignKey(ProjectImage, null=True)
  thumbnail = models.ImageField(upload_to=thumbnail_image_path, null=True)
  # tech = models.ManyToManyField(ProjectTech)
  # color = models.ManyToManyField(ProjectColor)
  # projimg = models.ImageField(upload_to='playground/%Y/%m/%d', null=True)
  objective = models.TextField()
  description = models.TextField()
  # motivation = models.TextField()
  solution = models.TextField(null = True, blank=True)
  # tech = models.TextField(null=True)
  #add colors, fonts? class/company? known bugs?
  slug = models.SlugField(max_length = 40, unique = True)
  
  def get_absolute_url(self):
    return "/playground/%s/" %(self.slug)

  def __unicode__(self):
    return self.title

  class Meta:
    ordering = ["-pub_date"]


#these could be many to many relationships instead to speed up the data
class ProjectTech(models.Model):
  project = models.ForeignKey(Project, null = True)
  # projects = models.ManyToManyField(Project, null=True)
  name = models.CharField(max_length = 200)
  # def __unicode__(self):
  #   return self.name

class ProjectColor(models.Model):
  project = models.ForeignKey(Project, null = True)
  # proj = models.ManyToManyField(Project)
  hexa = models.TextField(max_length=10)
    # def __unicode__(self):
  #   return self.color