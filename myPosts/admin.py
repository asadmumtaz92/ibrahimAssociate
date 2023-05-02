from django.contrib import admin

# Register your models here.

from django.contrib import admin
from . import models
# Register your models here.


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('post_id',)

admin.site.register(models.Posts, PostsAdmin,)
admin.site.register(models.Images, ImageAdmin,)
