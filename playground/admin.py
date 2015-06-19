from django.contrib import admin

# Register your models here.
from .models import Project, ProjectImage, ProjectTech, ProjectColor

# admin.site.register(Problem)
# admin.site.register(ProblemSet)


class ProjectImageInline(admin.TabularInline):
  model = ProjectImage
  extra = 3

class ProjectTechInline(admin.TabularInline):
  model = ProjectTech
  extra = 3

class ProjectColorInline(admin.TabularInline):
  model = ProjectColor
  extra = 3

class ProjectAdmin(admin.ModelAdmin):
  class Meta:
    model = Project

  prepopulated_fields = {"slug": ("title",)}

  fieldsets = [
    ('Project Information', {'fields': ['title', 'slug', 'objective', 'description', 'solution']}),
    ('Project Resources', {'fields':['pub_date', 'completion_date', 'projurl', 'thumbnail']}),
  ]

  # fieldsets = [
  #   ('Problem Info', {'fields': ['title', 'description', 'statement', 'many_attempts']}),
  #   # ('Required Files', {'fields': ['problem_files']}),
  #   ('Course Info', {'fields': ['course']}),
  # ]
  inlines = [ProjectImageInline, ProjectTechInline, ProjectColorInline]
  list_display = ('title', 'pub_date')

admin.site.register(Project, ProjectAdmin)

# admin.site.register(ProblemFile, ProblemFileAdmin)
# admin.site.register(Problem, ProblemAdmin)
# admin.site.register(ProblemSet, ProblemSetAdmin)