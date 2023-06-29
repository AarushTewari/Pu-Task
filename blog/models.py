from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, max_length=100)
    body = models.TextField()
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' : ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('blog-detail', args=(str(self.id)))