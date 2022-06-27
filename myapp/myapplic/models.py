from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_of_birth = models.DateTimeField('')
    
    def __str__(self):
       return f'{self.user.usernmae} Profile'
    birth_date = models.DateTimeField('date of birth')
