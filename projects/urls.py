from django.urls import path, include
from django.contrib import admin
from projects import views

urlpatterns = [
    path('', views.list_projects, name='projects'),
    path('<str:project_name>/', views.show_project, name='project')

]
