from django.shortcuts import render
from settings import MAX_LOADERS
import requests


def index(request):
    return render(request, 'priceweb/index.html')

def about(request):
    return render(request, 'priceweb/about.html')

def dori(request):
    return render(request, 'priceweb/dori.html')

def test(request):
    return render(request, 'priceweb/test.html')


def loadingscreens(request, index):
    i = int(index)

    if (i == MAX_LOADERS):
        prev = int(index) - 1
        next = 1
    elif (i == 1):
        prev = MAX_LOADERS
        next = int(index) + 1
    else:
        prev = int(index) - 1
        next = int(index) + 1

    last_loader =  str(prev)
    next_loader =  str(next)

    html = "priceweb/loaders/loading_screen_" + index + '.html'

    return render(request, html, context={'last_loader':last_loader, 'next_loader':next_loader})

def home(request):


    return render(request, 'priceweb/home.html')

def brewer(request):
    r = requests.get("https://api.punkapi.com/v2/beers/random")

    json = r.json()[0]

    method = json["method"]

    mash_temp = str(method["mash_temp"][0]["temp"]["value"]) + \
                " " + method["mash_temp"][0]["temp"]["unit"]
    fermentation_temp = str(method["fermentation"]["temp"]["value"]) + \
                        " " + method["fermentation"]["temp"]["unit"]

    temps = {'mash':mash_temp, 'fermentation':fermentation_temp}
    twist = method['twist']

    ingredients = json['ingredients']
    method = json['method']
    return render(request, 'priceweb/brewer.html', context={'json':json,
                                                            'ingredients':ingredients,
                                                            'method':method,
                                                            'temps':temps})