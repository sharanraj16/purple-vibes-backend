# Generated by Django 3.2.25 on 2025-04-30 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_rqdzyf', upload_to='images/'),
        ),
    ]
