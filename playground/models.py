
# Create your models here.
from django.db import models

# Create your models here.
class Project(models.Model):
  #to do: multiple image uploads
  title = models.CharField(max_length = 200)
  pub_date = models.DateTimeField('date added to site')
  projurl = models.URLField()
  completion_date = models.DateTimeField('date completed')
  # tech = models.ManyToManyField(ProjectTech)
  # color = models.ManyToManyField(ProjectColor)
  # projimg = models.ImageField(upload_to='playground/%Y/%m/%d', null=True)
  objective = models.TextField()
  description = models.TextField()
  motivation = models.TextField()
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


class ProjectImage(models.Model):
  proj = models.ForeignKey(Project, null=True)
  caption = models.TextField()
  projimg = models.ImageField(upload_to='playground/%Y/%m/%d', null=True) #ideally also include project name

  # def __unicode__(self):
  #   return self.url


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