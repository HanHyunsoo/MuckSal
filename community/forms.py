from django import forms
from .models import Post

class CreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea, label='')
    content = forms.CharField(widget=forms.Textarea, label='')
    
    class Meta:
        model = Post
        fields = ['title','content']
