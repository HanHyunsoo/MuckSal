from django.shortcuts import render, redirect
from .models import *
from .forms import FoodCreationForm, MealPlannerCreationForm


# Create your views here.
def create_meal_planner(request):
    rices = Food.objects.all().filter(category="01").order_by("?")
    soups = Food.objects.all().filter(category="02").order_by("?")
    side_dishes = Food.objects.all().filter(category="03").order_by("?")

    form = MealPlannerCreationForm()

    context = {
        "rices": rices,
        "soups": soups,
        "side_dishes": side_dishes,
        "form": form
    }
    return render(request, 'diet/test.html', context)