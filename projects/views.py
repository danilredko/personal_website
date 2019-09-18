from django.shortcuts import render

# Create your views here.
from django.urls import path, include
from django.contrib import admin


def list_projects(request):

    return render(request, 'projects.html')


def show_project(request, project_name):

    return render(request, project_name+'.html')
