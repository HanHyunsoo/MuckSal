from django.urls import path, include
import community.views

app_name = "community"
urlpatterns = [
    path('', community.views.community, name='community'),
    path('layout/', community.views.layout, name='layout'),
]