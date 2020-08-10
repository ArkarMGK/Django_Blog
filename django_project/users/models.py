from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    ## Profile will be deleted if the User is deleted (only one way from User)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ## install pillow to deal with ImageField
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'