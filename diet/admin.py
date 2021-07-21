from django.contrib import admin
from .models import Food, MealPlanner, FoodHashtag

# Register your models here.
admin.site.register(Food)
admin.site.register(FoodHashtag)
admin.site.register(MealPlanner)
