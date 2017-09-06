from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from settings import MAX_LOADERS
from scraper import ScraperObject as SO
import requests


def index(request):
    return render(request, 'priceweb/index.html')

def bestbuydata(request):
    return render(request, 'priceweb/bestbuy_tv_data.html')

def getTVData(request):

    smart_tv = SO(keyword='smart tv')
    curved_smart_tv = SO(keyword='curved smart tv')

    rate_trends = []

    data = smart_tv.search()
    curved_data = curved_smart_tv.search()


    hits_json = {'Sony':len(data['brands']['Sony']),
                  'Toshiba':len(data['brands']['Toshiba']),
                  'Samsung':len(data['brands']['Samsung']),
                  'LG':len(data['brands']['LG'])}

    curved_hits_json = {'Sony':len(curved_data['brands']['Sony']),
                  'Toshiba':len(curved_data['brands']['Toshiba']),
                  'Samsung':len(curved_data['brands']['Samsung']),
                  'LG':len(curved_data['brands']['LG'])}

    top_3_hits_json = {'Sony': len(data['top_3_brands']['Sony']),
                 'Toshiba': len(data['top_3_brands']['Toshiba']),
                 'Samsung': len(data['top_3_brands']['Samsung']),
                 'LG': len(data['top_3_brands']['LG'])}

    top_3_curved_hits_json = {'Sony': len(curved_data['top_3_brands']['Sony']),
                        'Toshiba': len(curved_data['top_3_brands']['Toshiba']),
                        'Samsung': len(curved_data['top_3_brands']['Samsung']),
                        'LG': len(curved_data['top_3_brands']['LG'])}


    return_obj = {'normal_hits': hits_json,
                  'curved_hits': curved_hits_json,
                  'top_3_hits': top_3_hits_json,
                  'top_3_curved_hits':top_3_curved_hits_json,
                  'rate_trends': data['ranks'],
                  'curved_rate_trends': curved_data['ranks'],
                  'review_trends':data['reviews'],
                  'curved_review_trends': curved_data['reviews']}

    return JsonResponse(return_obj)


def about(request):
    return render(request, 'priceweb/about.html')

def dori(request):
    return render(request, 'priceweb/dori.html')


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