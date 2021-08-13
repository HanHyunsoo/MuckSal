from django import forms
from .models import Food, MealPlanner


class FoodCreationForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'


class MealPlannerFoodListForm(forms.Form):
    rice = forms.ModelChoiceField(queryset=Food.objects.all().filter(category="01").order_by("?"), blank=True, required=False, empty_label="선택 안함")
    soup = forms.ModelChoiceField(queryset=Food.objects.all().filter(category="02").order_by("?"), blank=True, required=False, empty_label="선택 안함")
    side_dish1 = forms.ModelChoiceField(queryset=Food.objects.all().filter(category="03").order_by("?"), blank=True, required=False, empty_label="선택 안함")
    side_dish2 = forms.ModelChoiceField(queryset=Food.objects.all().filter(category="03").order_by("?"), blank=True, required=False, empty_label="선택 안함")
    side_dish3 = forms.ModelChoiceField(queryset=Food.objects.all().filter(category="03").order_by("?"), blank=True, required=False, empty_label="선택 안함")


class MealPlannerCreationForm(forms.ModelForm):
    class Meta:
        model = MealPlanner
        fields = '__all__'
