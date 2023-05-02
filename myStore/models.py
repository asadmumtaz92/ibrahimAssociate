from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Posts_1(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # demand = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts_1")
    # viewed = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


def get_image_filename(instance, filename):
    title = instance.post_id.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)


class Images_1(models.Model):
    post_id = models.ForeignKey(Posts_1, on_delete=models.CASCADE, related_name="images_1")
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image_1')
