from django import forms
from .models import *
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'PostTitle'}),
            'content': forms.Textarea(attrs={'class': 'PostContent'}),
            'photo': forms.FileInput(attrs={'class':'PostCreate'}),
        }
