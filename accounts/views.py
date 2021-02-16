from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
#def home (request):
#    return render (request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request, 'home.html')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {
        'form' : form
    })