# Generated by Django 5.0 on 2024-01-14 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_rename_desc_movie_desc_rename_image_movie_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='img',
            field=models.ImageField(upload_to='apps/img,null=true,blank=true'),
        ),
    ]
