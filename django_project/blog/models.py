from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now )  # to modify by the admin
    # auto_now=True       -->change datetime whenever the model is updated(modify)
    # auto_now_add = Ture -->set object created datetime only

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # if the User is deleted , the Post will be deleted(only one way)

    def __str__(self):
        return self.title