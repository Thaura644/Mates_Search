from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



class Notifications(models.Model):
    title=models.CharField(max_length=1044)
    user_id=models.CharField(max_length=250)
    sentTime=models.TimeField(default=timezone.now,null=True)
    details=models.CharField(max_length=1044)

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    university = models.CharField(max_length=1044)
    gender = models.CharField(max_length=50)
    accept_terms = models.BooleanField(default=False)

    