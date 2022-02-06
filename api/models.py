from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings
import os
# Create your models here.

class FishDetail(models.Model):
    fish_image=models.ImageField(upload_to="images/",null=True,blank=True)
    fish_name= models.CharField(max_length=200,null=True,blank=True)
    fish_species= models.CharField(max_length=200,null=True,blank=True)
    fish_weight = models.FloatField(null=True, blank=True, default=None)
    fish_length = models.FloatField(null=True, blank=True, default=None)
    fish_latitude = models.FloatField(null=True, blank=True, default=None)
    fish_longitude = models.FloatField(null=True, blank=True, default=None)
    uploaded_by=models.ForeignKey('auth.User', related_name='uploaded_by', on_delete=models.CASCADE)
    timestamp=models.DateField(auto_now_add=True)


    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        SIZE=140,140
        if self.fish_image:
            pic=Image.open(self.fish_image.path)
            pic.thumbnail(SIZE,Image.LANCZOS)
            pic.save(self.fish_image.path)
