import urllib2
from bs4 import BeautifulSoup
import mechanize
import re
from datetime import date

from settings import EMPTY_ATTRIBUTE_ERROR
from models import Television

class ScraperObject():
    """

    """

    def __init__(self, keyword=None):
        self.today = date.today()
        self.brands = {'Samsung':[],
                        'LG':[],
                       'Toshiba':[],
                       'Sony':[]}

        self.top3 = {'Samsung':[],
                        'LG':[],
                       'Toshiba':[],
                       'Sony':[]}

        self.top3Count = 0

        self.samsung_reg = re.compile('(?i)samsung')
        self.lg_reg = re.compile('(?i)lg')
        self.toshiba_reg = re.compile('(?i)toshiba')
        self.sony_reg = re.compile('(?i)sony')

        self.base_url = "https://www.bestbuy.com/"

        self.search_term = keyword


    def brandMatch(self, brand, item):
        self.brands[brand].append(item)
        if (self.top3Count < 3):
            self.top3[brand].append(item)
            self.top3Count += 1
            self.saveData(item, True)
        else:
            self.saveData(item, False)



    def findBrand(self, item):

        if self.samsung_reg.match(item['name']):
            self.brandMatch('Samsung', item)

        if self.lg_reg.match(item['name']):
            self.brandMatch('LG', item)

        if self.toshiba_reg.match(item['name']):
            self.brandMatch('Toshiba', item)

        if self.sony_reg.match(item['name']):
            self.brandMatch('Sony', item)


    def saveData(self, obj, top_3):
        search_rank = obj['search_rank']
        name = obj['name']
        rating = obj['rating']
        reviews = obj['reviews']
        Television.objects.create(search_rank=search_rank, search_date=self.today, search_term=self.search_term,
                                  name=name, rating=rating, reviews=reviews, top_3=top_3)





    def search(self):
        search_rank = 1
        ranks = []
        review_trend = []
        br = mechanize.Browser()
        br.open(self.base_url)

        br.select_form('frmSearch')
        br.form['st'] = self.search_term

        br.submit()

        r = br.response()

        soup = BeautifulSoup(r,'html.parser')
        items = soup.findAll('div', attrs={'class':'list-item-postcard'})
        for item in items:
                try:
                    name = item.find('div', attrs={'class':'sku-title'}).text
                    rating = item.find('span',attrs={'class':'star-rating-value'}).text
                    reviews = item.find('span',attrs={'class':'number-of-reviews'}).text

                    search_obj = {'search_rank':search_rank,
                                    'name':name,
                                    'rating':float(rating),
                                    'reviews':int(reviews)}

                    ranks.append([search_rank, float(rating)])
                    review_trend.append([search_rank, int(reviews)])

                    self.findBrand(search_obj)

                    search_rank += 1

                except AttributeError:
                    print EMPTY_ATTRIBUTE_ERROR


        return {'brands':self.brands, 'ranks':ranks, 'reviews':review_trend, 'top_3_brands':self.top3}

