from django import forms
from django.db.models import fields
from .models import Food
from django import forms

class CreateForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['title', 'body']

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')