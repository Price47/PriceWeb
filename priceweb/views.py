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

def getRequestData(json):

    method = json["method"]

    mash_temp = str(method["mash_temp"][0]["temp"]["value"]) + \
                " " + method["mash_temp"][0]["temp"]["unit"]
    fermentation_temp = str(method["fermentation"]["temp"]["value"]) + \
                        " " + method["fermentation"]["temp"]["unit"]

    temps = {'mash': mash_temp, 'fermentation': fermentation_temp}
    twist = method['twist']
    if twist == None:
        twist = 'Sorry, no creative twists for this beer!'

    ingredients = json['ingredients']
    method = json['method']

    return {'ingredients':ingredients, 'method':method, 'temps':temps,'twist':twist}


def brewer(request):

    if not request.GET.get('query_search'):
        url = "https://api.punkapi.com/v2/beers/random"
    else:
        url = "https://api.punkapi.com/v2/beers/?"
        name = request.GET.get('beer_name')
        abv_range = request.GET.get('abv_range')
        abv_query = request.GET.get('name_query')
        name_query = request.GET.get('name_query')
        abv_range_search = request.GET.get('abv_range_above')

        if name_query:
            if name:
                url += "beer_name=" + name + "&"

        elif abv_query:
            if abv_range_search=="less":
                url += "abv_lt=" + abv_range + "&"
            else:
                url += "abv_gt=" + abv_range + "&"

    if url == "https://api.punkapi.com/v2/beers/?":
        url = "https://api.punkapi.com/v2/beers/random"

    print url
    r = requests.get(url)

    json = r.json()[0]

    data = getRequestData(json)

    return render(request, 'priceweb/brewer.html', context={'json':json,
                                                            'ingredients':data['ingredients'],
                                                            'method':data['method'],
                                                            'temps':data['temps'],
                                                            'twist':data['twist']})