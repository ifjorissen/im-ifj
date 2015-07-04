from django.db import models
from django.utils import timezone

class Tag(models.Model):
  content = models.CharField(max_length=200, unique=True, default=None)
  slug = models.SlugField(max_length=200, unique=True)
  created_on  = models.DateTimeField( default=timezone.now)

  def __str__(self):
      return self.slug

  def get_absolute_url(self):
      # return reverse("tag_index", kwargs={"slug": self.slug})
      return "/blog/tagged/%s/" % (self.slug)


# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length = 200)
  pub_date = models.DateTimeField()
  text = models.TextField()
  tags = models.ManyToManyField(Tag, blank=True)
  slug = models.SlugField(max_length = 200, unique = True)
  
  def get_absolute_url(self):
    return "/blog/%s/" % (self.slug)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ["-pub_date"]