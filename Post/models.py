from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Post(models.Model):

    def __str__(self):
        return self
    

class Comment(models.Model):

    def __str__(self):
        return self
    

class Reply(models.Model):

    def __str__(self):
        return self