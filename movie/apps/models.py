from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=200)
    desc=models.CharField(max_length=200)
    year=models.IntegerField()
    img=models.ImageField(upload_to="apps/img,null=true,blank=true")
