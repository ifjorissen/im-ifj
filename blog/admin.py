from .models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Post, PostAdmin)
