from django import forms
from django.db.models import fields
from django.forms.widgets import TextInput, Textarea, Widget
from .models import Recipe
from django import forms

class CreateRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'body', 'ingredient']
        widgets ={
            'title' : TextInput(attrs={
                'class' : "form-control",
                'style' : 'max-width : 500px; text-align : center; margin : 50px;',
                'placeholder': '음식 이름'
            }),
            'body': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 500px; text-align : center;margin : 50px;',
                'placeholder': '조리법'
            }),
            'ingredient': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px; text-align : center;margin : 50px;',
                'placeholder': '재료'
            }),
        }

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')