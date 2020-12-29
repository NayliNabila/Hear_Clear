from django.http import HttpResponse
from .models import HearClear
from django.shortcuts import render

# Create your views here.
def home (request):
    pages = HearClear.objects.all()
    return render(request, 'home.html', {'pages' : pages})

def aboutme (request):
    return render(request, 'aboutme.html')

def base(request):
    return render(request, 'base.html')

def comments(request):
    return render(request, 'comments.html')