from django import forms
from .models import Food, MealPlanner


class FoodCreationForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'


class MealPlannerCreationForm(forms.ModelForm):
    rices = forms.ModelChoiceField(queryset=Food.objects.all().filter(category="01").order_by("?"))

    class Meta:
        model = MealPlanner
        fields = '__all__'
