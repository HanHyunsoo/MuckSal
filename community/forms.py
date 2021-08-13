from django import forms
from .models import Post,Comment



class CommentForm(forms.ModelForm):
    Comment = forms.CharField(max_length=200, label="댓글") 
    class Meta:
        model = Comment
        fields = ['text']
