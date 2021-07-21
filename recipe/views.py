from django.shortcuts import render, redirect,get_object_or_404
from django.http import request


# Create your views here.

def explain(request):
    return render(request, 'recipe/explain.html')
