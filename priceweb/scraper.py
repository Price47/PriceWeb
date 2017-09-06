import urllib2
from bs4 import BeautifulSoup
import mechanize
import re

from settings import EMPTY_ATTRIBUTE_ERROR

class ScraperObject():
    """

    """

    def __init__(self, brand=None, keyword=None):
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

        self.search_brands = brand
        self.search_term = keyword


    def findBrand(self, item):

        if self.samsung_reg.match(item['name']):
            self.brands['Samsung'].append(item)
            if(self.top3Count<3):
                self.top3['Samsung'].append(item)
                self.top3Count+=1

        if self.lg_reg.match(item['name']):
            self.brands['LG'].append(item)
            if (self.top3Count < 3):
                self.top3['LG'].append(item)
                self.top3Count += 1

        if self.toshiba_reg.match(item['name']):
            self.brands['Toshiba'].append(item)
            if (self.top3Count < 3):
                self.top3['Toshiba'].append(item)
                self.top3Count += 1

        if self.sony_reg.match(item['name']):
            self.brands['Sony'].append(item)
            if (self.top3Count < 3):
                self.top3['Sony'].append(item)
                self.top3Count += 1

    def getData(self, soup):
        ranks = [[]]
        review_trend = [[]]
        search_rank = 1

        for item in soup:
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

                # search_results.append(search_obj)

                    self.findBrand(search_obj)

                    search_rank += 1
                except AttributeError:
                    print EMPTY_ATTRIBUTE_ERROR

        return {'brands': self.brands, 'ranks': ranks, 'reviews': review_trend}


    def search(self):
        search_rank = 1
        search_results = []
        ranks = [[]]
        review_trend = [[]]
        br = mechanize.Browser()
        br.open(self.base_url)
        top_3_brands = {'Samsung':[],
                        'LG':[],
                       'Toshiba':[],
                       'Sony':[]}

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