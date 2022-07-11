from distutils.command.upload import upload
from email.policy import default
from operator import mod
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import datetime
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
import jsonfield

class Notifications(models.Model):
    title=models.CharField(max_length=1044,null=True)
    user_id=models.CharField(max_length=250)
    sentTime=models.TimeField(default=timezone.now)
    details=models.CharField(max_length=1044)
    date=models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    university = models.CharField(max_length=1044)
    gender = models.CharField(max_length=50)
    accept_terms = models.BooleanField(default=False)

class Userprofile(models.Model):
    user_id=models.CharField(max_length=250)
    profile_thumb = models.ImageField(upload_to="profile_images",default="../Myapp/static/images/profile.png")
    profile_img = ImageSpecField(source='profile_thumb',
                                           processors=[ResizeToFill(100, 50)],
                                           format='JPEG',
                                           options={'quality': 60})
    age = models.IntegerField(default=0)
    about = models.CharField(max_length=10044)
    interests = jsonfield.JSONField()
    height  =models.IntegerField()
    status = models.CharField(max_length=1044)
    phone_number = models.IntegerField()
    location = models.CharField(max_length=1044)
    languages = jsonfield.JSONField()

    def __str__(self):
        return self.user_id
    


    