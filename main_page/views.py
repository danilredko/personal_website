from django.shortcuts import render

# Create your views here.


def resume(request):

    return render(request, 'resume.html')


def main_page(request):

    return render(request, 'base.html')