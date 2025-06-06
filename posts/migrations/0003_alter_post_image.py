# Generated by Django 5.2 on 2025-05-01 14:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='default_post_x90pun', max_length=255, null=True, verbose_name='image'),
        ),
    ]
