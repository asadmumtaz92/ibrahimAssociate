from django.contrib import admin
from . import models
# Register your models here.


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('post_id',)

admin.site.register(models.Posts_1, PostsAdmin,)
admin.site.register(models.Images_1, ImageAdmin,)
