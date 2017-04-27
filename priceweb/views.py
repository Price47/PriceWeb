from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'priceweb/index.html')

def about(request):
    return render(request, 'priceweb/about.html')

def sidebar(request):
    return render(request, 'priceweb/sidebar.html')