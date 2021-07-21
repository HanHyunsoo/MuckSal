from django.urls import path, include
import recipe.views

app_name = "recipe"
urlpatterns = [
    path('explain/', recipe.views.explain, name="explain"),
]