from django import forms
from .models import SongFile

class SongForm(forms.ModelForm):
    class Meta:
        model = SongFile
        fields = ('title', 'audio')