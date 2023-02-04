from django.forms import forms, ModelForm

from .models import *


class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'tags', 'img_name']
