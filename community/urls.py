from django.urls import path, include
import community.views

app_name = "community"
urlpatterns = [
    path('', community.views.community, name='community'),
    path('new/create/', community.views.create, name ="create"),
    path('detail/<str:id>/', community.views.detail , name = "detail"),

]