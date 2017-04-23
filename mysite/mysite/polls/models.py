from __future__ import unicode_literals
from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    data = models.DateTimeField('date_published')
    def __str__(self):
        return self.title
class NiemPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    data = models.DateTimeField('date_published')


