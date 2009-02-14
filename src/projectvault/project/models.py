from django.db import models

from django.contrib.auth.models import User
import os
from django.conf import settings

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    author = models.ForeignKey(User)
    short_description = models.CharField(max_length=255)
    weight = models.IntegerField(default=0)
    
    class Meta:
        unique_together = (['title', 'author'],)

class RepresentationalImage(models.Model):
    project = models.ForeignKey(Project)
    text = models.TextField()
    slug = models.SlugField()
    image = models.ImageField(upload_to=os.path.join(settings.UPLOAD_DIR,'featureimages'), max_length=255)
    weight = models.IntegerField(default=0)

    class Meta:
        ordering = ['weight', 'id']


class Feature(models.Model):
    project = models.ForeignKey(Project)
    text = models.TextField()
    slug = models.SlugField()
