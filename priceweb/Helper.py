from datetime import date, datetime
from django.http import HttpResponse

from models import Television


class HelperObject():

    def __init__(self):
        self.today = date.today()

    def clearTodaysData(self):
        Television.objects.filter(search_date=self.today).delete()

    def lowestDate(self):

        return Television.objects.all().values_list('search_date', flat=True).order_by('search_date')[0]

    def highestDate(self):

        return Television.objects.all().values_list('search_date', flat=True).order_by('-search_date')[0]


    def sumBrands(self, dataset, key):
        return {'Sony': len(dataset[key]['Sony']),
                'Toshiba': len(dataset[key]['Toshiba']),
                'Samsung': len(dataset[key]['Samsung']),
                'LG': len(dataset[key]['LG'])}


    def sumDBBrands(self, base_query):

        return {'Sony': len(base_query.filter(name__icontains="sony")),
                'Toshiba': len(base_query.filter(name__icontains="toshiba")),
                'Samsung': len(base_query.filter(name__icontains="samsung")),
                'LG': len(base_query.filter(name__icontains="lg"))}


    def retrieveData(self, date):
        smart_tv = Television.objects.filter(search_term='smart tv').filter(search_date=date)
        curved_smart_tv = Television.objects.filter(search_term='curved smart tv').filter(search_date=date)

        hits_json = self.sumDBBrands(smart_tv)
        curved_hits_json = self.sumDBBrands(curved_smart_tv)
        top_3_hits_json = self.sumDBBrands(smart_tv.filter(top_3=True))
        top_3_curved_hits_json = self.sumDBBrands(curved_smart_tv.filter(top_3=True))

        rank_trend = list(smart_tv.values_list('search_rank', 'rating'))
        curved_rank_trend = list(curved_smart_tv.values_list('search_rank', 'rating'))

        review_trend = list(smart_tv.values_list('search_rank', 'reviews'))
        curved_review_trend = list(curved_smart_tv.values_list('search_rank', 'reviews'))

        return_obj = {'normal_hits': hits_json,
                      'curved_hits': curved_hits_json,
                      'top_3_hits': top_3_hits_json,
                      'top_3_curved_hits': top_3_curved_hits_json,
                      'rate_trends': rank_trend,
                      'curved_rate_trends': curved_rank_trend,
                      'review_trends': review_trend,
                      'curved_review_trends': curved_review_trend}

        return return_obj


    def writeCSVData(self, writer, search_term, base_query, top_3, ranks, reviews, search_date):
        writer.writerow([search_term,search_date])
        writer.writerow(['Top 3 Search Results'])
        writer.writerow(['Search Rank', 'Name', 'Rating', 'Reviews'])
        for i in top_3:
            writer.writerow([str(i.search_rank), str(i.name), str(i.rating), str(i.reviews)])
        writer.writerow(['Search Results'])
        writer.writerow(['Search Rank', 'Name', 'Rating', 'Reviews'])
        for i in base_query:
            writer.writerow([str(i.search_rank), str(i.name), str(i.rating), str(i.reviews)])
        writer.writerow(['Ranking Search Trend'])
        writer.writerow(['Search Rank', 'Rating'])
        for i in ranks:
            writer.writerow([str(i[0]), str(i[1])])
        writer.writerow(['Review Search Trend'])
        writer.writerow(['Search Rank', 'Reviews'])
        for i in reviews:
            writer.writerow([str(i[0]), str(i[1])])


    def formatCSVData(self, search_term, writer, search_date):

        base_query = Television.objects.filter(search_date=search_date).filter(search_term=search_term)
        top_3 = base_query.filter(top_3=True)
        ranks = base_query.values_list("search_rank","rating")
        reviews = base_query.values_list("search_rank", "rating")

        self.writeCSVData(writer, search_term, base_query, top_3, ranks, reviews, search_date)