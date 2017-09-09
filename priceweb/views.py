from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from settings import MAX_LOADERS
from scraper import ScraperObject as SO
import requests
import csv
from datetime import datetime, date
from celery.schedules import crontab
from celery.task import periodic_task

from Helper import  HelperObject

helper = HelperObject()


@periodic_task(run_every=crontab(hour=1, minute=30))
def update_bestbuy_snapshot():
    helper.clearTodaysData()

    SO(keyword='smart tv').search()
    SO(keyword='curved smart tv').search()

def index(request):
    return render(request, 'priceweb/index.html')

def bestbuydata(request):
    now = datetime.now()
    collected = "%d-%d-%d"%(now.month, now.day, now.year)
    return render(request, 'priceweb/bestbuy_tv_data.html', context={'date':collected})

def getTVData(request):

    helper.clearTodaysData()

    smart_tv = SO(keyword='smart tv')
    curved_smart_tv = SO(keyword='curved smart tv')

    smart_tv.search()
    curved_smart_tv.search()

    return_obj = helper.retrieveData()

    return JsonResponse(return_obj)


def savedTVData(request, search_date=None):
    if(search_date==None):
        search_date = date.today()
    else:
        datetime.strptime(search_date,"%Y-%m-%d").date()
    return_obj = helper.retrieveData(search_date)

    return JsonResponse(return_obj)

def getTvDataCSV(request):
    d = datetime.now()
    unique_string = "%d%d%d%d%d%d" % (d.year, d.month, d.day, d.hour, d.minute, d.second)

    filename = "Data_" + unique_string + ".csv"

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + filename

    writer = csv.writer(response)

    helper.formatCSVData('smart tv', writer)
    helper.formatCSVData('curved smart tv', writer)

    response.set_cookie(key='JSANIMATORCHECK', value='csv_download_complete')

    return response


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