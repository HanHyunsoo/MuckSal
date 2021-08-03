from django.urls import path, include
from . import views
from .views import *

app_name = "accounts"
urlpatterns = [
    path('signup/',signup, name='signup'),
    path('login/',login, name='login'),
    path('logout/',logout, name='logout'),
]