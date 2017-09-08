from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from settings import MAX_LOADERS
from scraper import ScraperObject as SO
import requests
import csv
from datetime import datetime

from models import Television

def index(request):
    return render(request, 'priceweb/index.html')

def bestbuydata(request):
    now = datetime.now()
    collected = "%d/%d/%d"%(now.month, now.day, now.year)
    return render(request, 'priceweb/bestbuy_tv_data.html', context={'date':collected})


def sumBrands(dataset,key):
    return {'Sony': len(dataset[key]['Sony']),
             'Toshiba': len(dataset[key]['Toshiba']),
             'Samsung': len(dataset[key]['Samsung']),
             'LG': len(dataset[key]['LG'])}

def sumDBBrands(base_query):

    return {'Sony':len(base_query.filter(name__icontains="sony")),
            'Toshiba': len(base_query.filter(name__icontains="toshiba")),
            'Samsung': len(base_query.filter(name__icontains="samsung")),
            'LG':len(base_query.filter(name__icontains="lg"))}




def getTVData(request):

    smart_tv = SO(keyword='smart tv')
    curved_smart_tv = SO(keyword='curved smart tv')

    data = smart_tv.search()
    curved_data = curved_smart_tv.search()

    hits_json = sumBrands(data,'brands')
    curved_hits_json = sumBrands(curved_data, 'brands')
    top_3_hits_json = sumBrands(data, 'top_3_brands')
    top_3_curved_hits_json = sumBrands(curved_data, 'top_3_brands')

    return_obj = {'normal_hits': hits_json,
                  'curved_hits': curved_hits_json,
                  'top_3_hits': top_3_hits_json,
                  'top_3_curved_hits':top_3_curved_hits_json,
                  'rate_trends': data['ranks'],
                  'curved_rate_trends': curved_data['ranks'],
                  'review_trends':data['reviews'],
                  'curved_review_trends': curved_data['reviews']}

    return JsonResponse(return_obj)


def savedTVData(request):
    smart_tv = Television.objects.filter(search_term='smart tv')
    curved_smart_tv = Television.objects.filter(search_term='curved smart tv')


    hits_json = sumDBBrands(smart_tv)
    curved_hits_json = sumDBBrands(curved_smart_tv)
    top_3_hits_json = sumDBBrands(smart_tv.filter(top_3=True))
    top_3_curved_hits_json = sumDBBrands(curved_smart_tv.filter(top_3=True))

    rank_trend = list(smart_tv.values_list('search_rank','rating'))
    curved_rank_trend = list(curved_smart_tv.values_list('search_rank','rating'))

    review_trend = list(smart_tv.values_list('search_rank','reviews'))
    curved_review_trend = list(curved_smart_tv.values_list('search_rank','reviews'))


    return_obj = {'normal_hits': hits_json,
                  'curved_hits': curved_hits_json,
                  'top_3_hits': top_3_hits_json,
                  'top_3_curved_hits':top_3_curved_hits_json,
                  'rate_trends': rank_trend,
                  'curved_rate_trends': curved_rank_trend,
                  'review_trends':review_trend,
                  'curved_review_trends': curved_review_trend}


    print return_obj


    return JsonResponse(return_obj)



def getTvDataCSV(request):
    obj = SO(keyword='smart tv')
    data = obj.search()
    top3 = data['top_3_brands']
    brands = data['brands']
    ranks = data['ranks']
    review = data['reviews']
    d = datetime.now()
    unique_string = "%d%d%d%d%d%d" % (d.year, d.month, d.day, d.hour, d.minute, d.second)

    filename = "Data_" + unique_string + ".csv"

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + filename

    writer = csv.writer(response)

    writer.writerow(['Smart TV'])
    writer.writerow(['Top 3 Search Results'])
    writer.writerow(['Search Rank','Name','Rating','Reviews'])
    for key in ['Samsung', 'Sony', 'LG', 'Toshiba']:
        for i in top3[key]:
            writer.writerow([str(i['search_rank']),str(i['name']),str(i['rating']),str(i['reviews'])])
    writer.writerow(['Search Results'])
    writer.writerow(['Search Rank','Name','Rating','Reviews'])
    for key in ['Samsung', 'Sony', 'LG', 'Toshiba']:
        for i in brands[key]:
            writer.writerow([str(i['search_rank']),str(i['name']),str(i['rating']),str(i['reviews'])])
    writer.writerow(['Ranking Search Trend'])
    writer.writerow(['Search Rank','Rating'])
    for i in ranks:
        writer.writerow([str(i[0]),str(i[1])])
    writer.writerow(['Review Search Trend'])
    writer.writerow(['Search Rank','Reviews'])
    for i in review:
        writer.writerow([str(i[0]),str(i[1])])

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