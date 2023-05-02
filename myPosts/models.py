from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    demand = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    viewed = models.IntegerField()
    size = models.CharField(choices=(
            ('4M', "4 Marla"),
            ('5M', "5 Marla"),
            ('8M', "8 Marla"),
            ('10M', "10 Marla"),
            ('1K', "1 Kanal"),
            ('2K', "2 Kanal"),
        ),
        max_length = 3
    )
    sector = models.CharField(choices=(
            ('A', "Sector A"),
            ('B', "Sector B"),
            ('B1', "Sector B1"),
            ('B2', "Sector B2"),
            ('C', "Sector C"),
            ('C1', "Sector C1"),
            ('C2', "Sector C2"),
            ('C3', "Sector C3"),
            ('D', "Sector D"),
            ('E', "Sector E"),
            ('F', "Sector F"),
            ('F1', "Sector F1"),
            ('G', "Sector G"),
            ('H', "Sector H"),
            ('I', "Sector I"),
            ('J', "Sector J"),
            ('K', "Sector K"),
            ('L', "Sector L"),
            ('M', "Sector M"),
            ('N', "Sector N"),
            ('O', "Sector O"),
            ('P', "Sector P"),
        ),
        max_length = 2
    )
    type = models.CharField(choices=(
            ('R', "Residential"),
            ('C', "Commercial"),
        ),
        max_length = 1
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_image_filename(instance, filename):
        title = instance.post.title
        slug = slugify(title)
        return "post_images/%s-%s" % (slug, filename)



# MODEL FOR IMAGES
# class Images(models.Model):
#     post_id = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="images")
#     image = models.ImageField(upload_to=get_image_filename, related_name='images')
