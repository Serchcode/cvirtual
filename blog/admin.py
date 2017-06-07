from django.contrib import admin
from django.db import models
from .models import Post
from pagedown.widgets import AdminPagedownWidget


class Post_content(admin.ModelAdmin):
	formfield_overrides = {models.TextField: {'widget': AdminPagedownWidget }}
	prepopulated_fields = {"slug": ("post_title",)}


   
admin.site.register(Post,Post_content)

