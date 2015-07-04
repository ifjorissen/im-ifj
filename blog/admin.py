from .models import Post, Tag
from django.contrib import admin
from django.forms import ModelForm

class TagAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("content",)}

class TagInline(admin.TabularInline):
  model = Post.tags.through
  extra = 3

class PostAdmin(admin.ModelAdmin):
  class Meta:
    model = Post

  fieldsets = [
    ('Post Content', {'fields': ['title', 'text']}),
    ('Post Info', {'fields':['pub_date', 'slug', 'tags']}),
  ]
  # inlines = [TagInline]
  filter_horizontal = ['tags']
  list_display = ('title', 'pub_date')
  prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
