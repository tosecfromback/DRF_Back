from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Question(models.Model):
    # title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content