from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','writer','content','image']

class CommentForm(forms.ModelForm):
    Comment = forms.CharField(max_length=200, label="댓글") 
    class Meta:
        model = Comment
        fields = ['text']
