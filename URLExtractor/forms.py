# forms.py
from django import forms

class URLForm(forms.Form):
    url = forms.URLField(label='',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL here'}))
