from django.forms import ModelForm
from .models import Comments



class CommentForm(ModelForm):
    model = Comments
    fields = ('text')
