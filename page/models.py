from django.db import models
from django.contrib.auth.models import User
#import librosa

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
    
    #fileduration=librosa.get_duration(filename=self.title)
    #print (fileduration)

    #  @property
    #def filesize(self):
    #    x = self.file.size
    #    y = 512000
    #    if x < y :
    #        value = round (x/1000,2)
    #        ext = 'kb'
    #    elif x < y*1000 :
    #        value = round (x/1000000, 2)
    #        ext = 'Mb'
    #    else:
    #        value = round (x/1000000000, 2)
    #        ext = 'Gb'
    #    return str(value)+ext