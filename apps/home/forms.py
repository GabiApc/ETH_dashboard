from unicodedata import name
from django import forms
from django.forms import ModelForm
from .models import Voluntari


#formular date voluntari
class FormularVol(ModelForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    
    class Meta:
        model = Voluntari
        fields = ('first_name','last_name')
