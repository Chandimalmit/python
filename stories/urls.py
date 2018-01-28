from django.contrib import admin
from django.urls import path
from . import views

app_name = 'stories'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('add', views.CreateStory.as_view(), name='add-story'),
    path('ratings', views.RatingView.as_view(), name='rating'),
]
