from django.urls import path, include
import recipe.views

app_name = "recipe"
urlpatterns = [
    path('explain/', recipe.views.explain, name="explain"),
    path('search/', recipe.views.search, name = "serach"),
    path('add/', recipe.views.add, name = "add"),
    path('list/', recipe.views.list, name = "list"),
    path('add/create/', recipe.views.create, name = "create"),
]