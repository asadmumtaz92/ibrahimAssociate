# Generated by Django 4.2 on 2023-05-01 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import myStore.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('demand', models.IntegerField()),
                ('viewed', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=myStore.models.get_image_filename, verbose_name='Image')),
                ('ad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_1', to='myStore.posts_1')),
            ],
        ),
    ]