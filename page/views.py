from django.http import HttpResponse
from .models import HearClear
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
#from django.http import Http404

from .form import SongForm
from .models import SongFile
from .songinfo import SongInfo

# Create your views here.
def home (request):
    songs = SongFile.objects.all()
    return render(request, 'home.html', {
        'songs' : songs
    })

def songdetails (request, pk):
    songfile = get_object_or_404(SongFile, pk=pk)
    SongInfoResult = SongInfo ()
    return render (request, 'songdetails.html', {'songfile' : songfile})

def result (self):
    #self.songfile = song
    SongInfoResult = SongInfo ()
    return render (request, 'songdetails.html')

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