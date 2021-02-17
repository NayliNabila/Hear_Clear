from django.http import HttpResponse
from .models import HearClear
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .form import SongForm
from .models import SongFile

# Create your views here.
def home (request):
    songs = SongFile.objects.all()
    return render(request, 'home.html', {
        'songs' : songs
    })

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
        form = SongForm(request.POST, request.FILES, pk=song_id)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SongForm()
        return render(request, 'upload.html', {
        'form' : form
    })

def songs (request):
    return render(request, 'songs.html')