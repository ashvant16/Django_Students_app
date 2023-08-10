from django import forms
from .models import *

class AudioForm(forms.ModelForm):
    class Meta:
       model= MusicFiles
       fields=['title','artist','song']