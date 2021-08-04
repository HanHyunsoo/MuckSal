from django.shortcuts import render, redirect,get_object_or_404
from django.http import request
from .models import Food


# Create your views here.

def explain(request):
    return render(request, 'recipe/explain.html')

def search(request):
    return render(request, 'recipe/search.html')

def add(request):
    return render(request, 'recipe/add.html')

def list(request):
    foods = Food.objects
    return render(request, 'recipe/list.html', {'foods':foods})

def create(request):
    food = Food()
    food.title = request.POST['title']
    food.body = request.POST['body']
    food.save()
    return redirect('recipe/add.html')