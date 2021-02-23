from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.core.files.images import ImageFile

import librosa 
import librosa.display
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

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
    audio = models.FileField(upload_to= 'songs')
    image = models.ImageField(upload_to='audioimage/image')
    date = models.DateTimeField(default=timezone.now)
    duration = models.CharField(max_length=10)
    samp_freq = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('songfile-detail', kwargs={'pk': self.pk})

    def save (self, *args, **kwargs):
        super(SongFile,self).save(*args, **kwargs)
        dir_image = "./media/audioimage/image"
        imagePath = dir_image + str(timezone.now()) + ".png"
        #img =Audio.open(self.image.path)
        audio, sr = librosa.load(self.audio.path)
        fig, ax = plt.subplots(1)
        ax.set(title='testing')
        ax.label_outer()
        librosa.display.waveplot(audio, sr=sr, ax=ax)
        plt.show()
        plt.savefig(imagePath)
        self.image = ImageFile(open(imagePath, 'rb'))
        self.duration = librosa.get_duration(y=audio,sr=sr)
        
        file_size_byte = os.path.getsize(file)
        file_size = file_size_byte/1024
                
        super(SongFile,self).save(*args, **kwargs)
        #self.image.path = plt.savefig(self.image.path + str(timezone.now()) + ".png")
        #self.image = y
        #super(SongFile,self).save(self.image.path)
        #self.image.save(image)
        #self.image = (imagePath)
        #img=Image.open(self.image.path)
        #img.save(self.image.path)
        #return self.image.url


"""class SongData(models.Model):
    titlee = models.CharField(max_length = 100)
    filetypee = models.FileField(upload_to= 'songs/filetype/')
    duration = models.CharField(max_length=10)
    samp_freq = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    
    def __str__(self):
        return self.titlee"""

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
