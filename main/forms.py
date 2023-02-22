from django.forms import forms, ModelForm

from .models import *


class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'tags', 'img_name']

    def clean_title(self):
        title = self.cleaned_data['title']
        if Post.objects.filter(title=title).exists():
            raise forms.ValidationError("This name already exists")
        return title
