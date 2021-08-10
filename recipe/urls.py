from django.urls import path, include
import recipe.views

app_name = "recipe"
urlpatterns = [
    path('foodinfo/<str:foodid>/', recipe.views.foodinfo, name = 'foodinfo'),
    path('list/', recipe.views.list, name = 'list'),
    path('new/', recipe.views.new, name = 'new'),
    path('create/', recipe.views.create, name ='create'),
    path('search/', recipe.views.search, name='search'),
    path('postcreate/', recipe.views.postcreate, name='postcreate'),
]