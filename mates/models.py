from django.db import models
from django.utils import timezone

class Notifications(models.Model):
    title=models.CharField(max_length=1044)
    user_id=models.CharField(max_length=250)
    sentTime=models.TimeField(default=timezone.now,null=True)
    details=models.CharField(max_length=1044)

    def __str__(self):
        return self.title

