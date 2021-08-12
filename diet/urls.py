from django.urls import path, include
from .views import *

app_name = "diet"
urlpatterns = [
    path('create/', create_meal_planner, name='create'),
    path('mymealplanner/', check_my_meal_planners, name='my_meal_planner'),
    # path('test/', test, name="test"),
]