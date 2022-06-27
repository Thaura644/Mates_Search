from django.contrib import admin
from .models import Profile
from .models import users


admin.site.register(Profile)
admin.site.register(users)
# Register your models here.
