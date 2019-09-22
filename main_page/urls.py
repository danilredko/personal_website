from django.urls import path, include
from django.contrib import admin
from main_page import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('resume/', views.resume, name='resume')
]
