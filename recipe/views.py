from recipe.forms import CreateRecipe
from django.shortcuts import render, redirect,get_object_or_404
from django.http import request
from .models import Recipe
from .forms import PostSearchForm
from django.db.models import Q

# Create your views here.

def foodinfo(request, foodid):
    food = get_object_or_404(Recipe, id = foodid)
    return render(request, 'recipe/foodinfo.html', {'food':food})

def list(request):
    foods = Recipe.objects
    return render(request, 'recipe/list.html', {'foods':foods})

def new(request):
    return render(request, 'recipe/new.html')

def create(request):
    if request.method == 'POST':
        form = CreateRecipe(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.save()
            return redirect('recipe:list')

    else:
        form = CreateRecipe()
        return render(request, 'recipe/create.html', {'form':form})

def search(request):
    return render(request, 'recipe/search.html')



# def postcreate(request):
#     blog = Recipe()
#     blog.title = request.GET['title']
#     blog.body = request.GET['body']
#     blog.save()
#     return redirect('recipe:list')

def search(request):
    foods = Recipe.objects.all().order_by('-id')

    q = request.POST.get('q', "") 

    if q:
        foods = foods.filter(title__icontains=q)
        return render(request, 'recipe/search.html', {'foods' : foods, 'q' : q})
    
    else:
        return render(request, 'recipe/search.html')