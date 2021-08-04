from django import forms
from .models import Food, MealPlanner


class FoodCreationForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'


class MealPlannerFoodListForm(forms.Form):
    rices = forms.ModelChoiceField(queryset=Food.objects.all().filter(category="01").order_by("?"))
    soups = forms.ModelChoiceField(queryset=Food.objects.all().filter(category="02").order_by("?"))
    side_dishes1 = forms.ModelChoiceField(queryset=Food.objects.all().filter(category="03").order_by("?"))
    side_dishes2 = forms.ModelChoiceField(queryset=Food.objects.all().filter(category="03").order_by("?"))
    side_dishes3 = forms.ModelChoiceField(queryset=Food.objects.all().filter(category="03").order_by("?"))


class MealPlannerCreationForm(forms.ModelForm):
    class Meta:
        model = MealPlanner
        fields = '__all__'
