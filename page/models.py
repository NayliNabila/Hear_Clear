from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class HearClear(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Type(models.Model):
    type = models.CharField(max_length = 10)

    def __str__(self):
        return self.type

class SongFile(models.Model):
    title = models.CharField(max_length = 100)
    filetype = models.FileField(upload_to= 'songs/filetype/')

    def __str__(self):
        return self.title