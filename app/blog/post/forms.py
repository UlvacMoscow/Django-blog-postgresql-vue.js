from .models import Comments
from django import forms
from .models import Post



class CommentForm(forms.ModelForm):
    model = Comments
    fields = ('text')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title']
