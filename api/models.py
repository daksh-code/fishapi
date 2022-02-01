from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class FishDetail(models.Model):
    uploaded_by=models.ForeignKey('auth.User', related_name='uploaded_by', on_delete=models.CASCADE)
    fish_image=models.ImageField(upload_to="fish_image",null=True,blank=True)
    fish_name= models.CharField(max_length=200,null=True,blank=True)
    fish_species= models.CharField(max_length=200,null=True,blank=True)
    fish_weight = models.FloatField(null=True, blank=True, default=None)
    fish_length = models.FloatField(null=True, blank=True, default=None)
    fish_latitude = models.FloatField(null=True, blank=True, default=None)
    fish_longitude = models.FloatField(null=True, blank=True, default=None)
    timestamp=models.DateField(auto_now_add=True)
