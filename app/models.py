from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=200, blank=True)
    cityname=models.CharField(max_length=100,blank=True)
    state=models.CharField(max_length=200,blank=True)
    address=models.CharField(max_length=200,blank=True)
    postal_code=models.IntegerField(default=0)
    age=models.IntegerField(default=18)
    profile_pic=models.ImageField(default="profile_images/Profile.jpg",null=True,blank=True,upload_to='profile_images/')

    def __str__(self):
        return str(self.user)
    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


