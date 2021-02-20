from django.http import HttpResponse
from .models import HearClear
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
#from django.http import Http404

from .form import SongForm
from .models import SongFile
from django.db import models
#from .models import ModelWithFileField
#from .songinfo import SongInfo
from django.views.generic import DetailView

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.core.files.images import ImageFile
import numpy as np
from io import BytesIO
import librosa 
import librosa.display
from django.core.files.storage import FileSystemStorage
import sys
import datetime
import os
from glob import glob

# Create your views here.
def home (request):
    songs = SongFile.objects.all()
    return render(request, 'home.html', {
        'songs' : songs
    })


def testing (request):
    #songfile = get_object_or_404(SongFile, pk=pk)
    #path = SongFile.objects.get(filetype)
    dir_image = "./media/audioimage"
    dir_sound = "./media/songs"
    audio_files = glob (dir_sound + "/*.wav")
    #sound =  os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/song/')
    audio, sr = librosa.load(audio_files[1])
    #time = np.arrange(0, len(audio))/sr
    fig, ax = plt.subplots(1)
    ax.set(title='Monophonic')
    ax.label_outer()
    librosa.display.waveplot(audio, sr=sr, ax=ax)
    plt.show()
    plt.savefig(dir_image + "/*.png")
    return render (request, 'testing.html')

def songdetails (request, pk):
    songfile = get_object_or_404(SongFile, pk=pk)
    #path = SongFile.objects.get(filetype)
    #songtitle = request.FileField
    dir_image = "./media/audioimage"
    dir_sound = "./media/songs" + songfile.audio
    #songtitle = ModelWithFileField(file_field=request.FILES['file'])
    #audio_files = glob (dir_sound + "/*.wav")
    audio_files = glob (dir_sound + ".png")
    audio, sr = librosa.load(audio_files)
    #time = np.arrange(0, len(audio))/sr
    fig, ax = plt.subplots(1)
    ax.set(title='Monophonic')
    ax.label_outer()
    librosa.display.waveplot(audio, sr=sr, ax=ax)
    plt.show()
    plt.savefig(dir_image + "/image.png")
    return render (request, 'songfile-detail.html', { 'songfile' : songfile})

"""class SongFileDetailView (DetailView):
    model = SongFile
    template_name = 'songfile-detail.html'
    fields = ['title','audio']

    def form_valid(self, form):

        Song = SongInfo(form.instance.audio)
        form.instance.image = Song[0]
        form.instance.duration = Song[1]
        form.instance.samp_freq = Song[2]
        
        return super().form_valid(form)"""


def aboutme (request):
    return render(request, 'aboutme.html')

def base(request):
    return render(request, 'base.html')

def comments(request):
    return render(request, 'comments.html')

def reply(request):
    return render(request, 'reply.html')

def upload (request):
    if request.method =='POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SongForm()
        return render(request, 'upload.html', {
        'form' : form
    })

#def songs (request):
#    return render(request, 'songs.html')

#class PostSongs():
#    model = Post
#    fields = ['title','content','audio']



"""    def form_valid(self, form):
        form.instance.author =self.request.user
        
        SoundResult =  Sound(form.instance.audio)
        form.instance.image = SoundResult[0]
        form.instance.duration = SoundResult[1]
        form.instance.samp_freq = SoundResult[2]
        
        return super().form_valid(form)"""