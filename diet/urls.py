from django.urls import path, include
from .views import *

app_name = "diet"
urlpatterns = [
    path('create/', create_meal_planner, name='create')
]