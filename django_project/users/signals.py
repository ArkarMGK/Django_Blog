## To automically create Profile when the new user is registered
## import signals inside ready function of apps.py
from django.db.models.signals import post_save    # signal when fires after an object is saved
from django.contrib.auth.models import User       
from django.dispatch import receiver
from .models import Profile

## Create Profile when User object is created
@receiver(post_save, sender=User)                             # when the User is saved 'post_save' signal is sent
def create_profile(sender, instance, created, **kwargs):      
    if created:                                               # if the instance of user is created
        Profile.objects.create(user=instance)                # create the Profile with that user instance (one to one Relationship) 

## Save Profile with that user instance
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


