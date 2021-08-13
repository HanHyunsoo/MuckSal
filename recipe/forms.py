from django import forms
from django.db.models import fields
from .models import Recipe
from django import forms

class CreateRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'body']

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')