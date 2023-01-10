from django.forms import forms, ModelForm

from .models import *


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['']