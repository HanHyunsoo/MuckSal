import json

from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from .models import *
from accounts.models import User
from .forms import FoodCreationForm, MealPlannerCreationForm, MealPlannerFoodListForm


# Create your views here.
def create_meal_planner(request):
    rices = Food.objects.all().filter(category="01").order_by("?")
    soups = Food.objects.all().filter(category="02").order_by("?")
    side_dishes = Food.objects.all().filter(category="03").order_by("?")
    foods = Food.objects.all()
    error_message = ""

    if request.method == "POST":
        form = MealPlannerFoodListForm(request.POST)
        if form.is_valid():
            meal_planner = MealPlannerCreationForm().save(commit=False)
            foods_form = [
                Food.objects.all().filter(food_name=form.cleaned_data['rice']).first(),
                Food.objects.all().filter(food_name=form.cleaned_data['soup']).first(),
                Food.objects.all().filter(food_name=form.cleaned_data['side_dish1']).first(),
                Food.objects.all().filter(food_name=form.cleaned_data['side_dish2']).first(),
                Food.objects.all().filter(food_name=form.cleaned_data['side_dish3']).first()
            ]   # 폼에서 입력받은 밥, 국, 반찬들(뒤에 first()쓴 이유는 None값을 받을수도 잇기 때문)
            # meal_planner.user = request.user
            if foods_form.count(None) == 5: # 입력받은 음식들이 전부 None이면 error_message에 내용을 추가한다
                error_message = "식판에 음식을 전부 선택하지 않으셨습니다. 다시 선택해 주세요."
            else:
                meal_planner.user = get_object_or_404(User, pk=1)   # 임시임 회원가입기능 완성되면 위 줄을 쓸것
                meal_planner.save()    # 일단 먼저 MealPlanner 모델을 먼저 만듬
                for food in foods_form:  # 그리고 폼에서 입력받은 음식들을 저장한 식판 모델에 m2m 저장
                    if food is not None:
                        meal_planner.foods.add(food)
                return redirect("diet:create")
    else:
        form = MealPlannerFoodListForm()

    context = {
        "rices": rices,
        "soups": soups,
        "side_dishes": side_dishes,
        "foods": foods,
        "form": form,
        "error_message": error_message,
    }
    return render(request, 'diet/create.html', context)


def check_my_meal_planners(request):
    my_meal_planners = MealPlanner.objects.filter(user=request.user)
    return render(request, 'diet/test2.html', {'planners': my_meal_planners})

#
# def test(request):
#     rices = Food.objects.all().filter(category="01").order_by("?")
#     soups = Food.objects.all().filter(category="02").order_by("?")
#     side_dishes = Food.objects.all().filter(category="03").order_by("?")
#     foods = Food.objects.all()
#     error_message = ""
#     form = MealPlannerFoodListForm()
#
#     context = {
#         "rices": rices,
#         "soups": soups,
#         "side_dishes": side_dishes,
#         "foods": foods,
#         "form": form,
#         "error_message": error_message,
#     }
#
#     return render(request, 'diet/create.html', context)
