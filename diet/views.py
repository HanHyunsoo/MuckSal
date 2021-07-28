from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from accounts.models import User
from .forms import FoodCreationForm, MealPlannerCreationForm, MealPlannerFoodListForm


# Create your views here.
def create_meal_planner(request):
    rices = Food.objects.all().filter(category="01").order_by("?")
    soups = Food.objects.all().filter(category="02").order_by("?")
    side_dishes = Food.objects.all().filter(category="03").order_by("?")

    if request.method == "POST":
        form = MealPlannerFoodListForm(request.POST)
        if form.is_valid():
            meal_planner = MealPlannerCreationForm().save(commit=False)
            foods = [
                Food.objects.all().get(food_name=form.cleaned_data['rices']),
                Food.objects.all().get(food_name=form.cleaned_data['soups']),
                Food.objects.all().get(food_name=form.cleaned_data['side_dishes1']),
                Food.objects.all().get(food_name=form.cleaned_data['side_dishes2']),
                Food.objects.all().get(food_name=form.cleaned_data['side_dishes3'])
            ]   # 폼에서 입력받은 밥, 국, 반찬들
            # meal_planner.user = request.user
            meal_planner.user = get_object_or_404(User, pk=1)   # 임시임 회원가입기능 완성되면 위 줄을 쓸것
            meal_planner.save()    # 일단 먼저 MealPlanner 모델을 먼저 만듬
            for food in foods:  # 그리고 폼에서 입력받은 음식들을 저장한 식판 모델에 m2m 저장
                meal_planner.foods.add(food)
            return redirect("diet:create")
    else:
        form = MealPlannerFoodListForm()

    context = {
        "rices": rices,
        "soups": soups,
        "side_dishes": side_dishes,
        "form": form,
    }
    return render(request, 'diet/test.html', context)


def check_my_meal_planners(request):
    my_meal_planners = MealPlanner.objects.filter(user=request.user)
    return render(request, 'diet/test2.html', {'planners': my_meal_planners})
