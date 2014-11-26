import json
import requests
from bs4 import BeautifulSoup

from models.Stock import Stock
from core.helpers import BaseHelper


class QueryHelper(BaseHelper):

    @classmethod
    def update_stock(cls, stock):
        params = {}
        params1, msg_yahoo = cls.get_yahoo_stats(stock, params)
        params2, msg_google = cls.get_yahoo_stats(stock, params)

        if params1 or params2:
            if params1:
                # The yahoo stats
                stock.PriceSales = params1['PriceSales']
                stock.TotalCashPerShare = params1['TotalCashPerShare']
                stock.BookValuePerShare = params1['BookValuePerShare']
                stock.ProfitMargin = params1['ProfitMargin']
                stock.TotalDebt = params1['TotalDebt']
                stock.code = params1['Symbol']
            if params2:
                # The google Stats
                stock.name = params2['Name']
                stock.price = params2['Price']
                stock.eps = params2['EPS']
                stock.pe = params2['PE']
                stock.dividend_yield = params2['DivYield']
                stock.shares = params2['Shares']
            # Put it in the DataBase
            stock.put()
            return [True, params['Symbol']+' has been updated']
        else:
            return [False, msg_yahoo, msg_google]

    @classmethod
    def create_stock(cls, stock):
        params = {}
        params1, msg_yahoo = cls.get_yahoo_stats(stock, params)
        params2, msg_google = cls.get_yahoo_stats(stock, params)

        if params1 and params2:
            new_stock = Stock(
                price_sale=params1['PriceSales'],
                TotalCashPerShare=params1['TotalCashPerShare'],
                BookValuePerShare=params1['BookValuePerShare'],
                ProfitMargin=params1['ProfitMargin'],
                TotalDebt=params1['TotalDebt'],
                code=params1['Symbol'],
                name=params2['Name'],
                price=params2['Price'],
                eps=params2['EPS'],
                pe=params2['PE'],
                dividend_yield=params2['DivYield'],
                shares=params2['Shares']
            )
            new_stock.put()
            return [True, params['Symbol']+' has been created']
        else:
            return [False, msg_yahoo, msg_google]

    @classmethod
    def get_yahoo_ks(cls, stock):
        url = "https://query.yahooapis.com/v1/public/yql?q=SELECT%20*%20FRO\
        M%20yahoo.finance.keystats%20WHERE%20symbol%3D'{}.AX'&format=json&di\
        agnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&c\
        allback=".format(stock)
        r = requests.get(url)
        ks = json.loads(r.text)['query']['results']['stats']
        if 'MarketCap' in ks:
            return ks
        else:
            return None

    @classmethod
    def get_yahoo_stats(cls, stock, params):
        ks = cls.get_ks(stock)
        if ks:
            params['PriceSales'] = ks['PriceSales']['content']
            params['TotalCashPerShare'] = ks['TotalCashPerShare']['content']
            params['BookValuePerShare'] = ks['BookValuePerShare']['content']
            params['ProfitMargin'] = ks['ProfitMargin']['content']
            params['TotalDebt'] = ks['TotalDebt']['content'] if 'content' in ks['TotalDebt'] else 'N/A'
            params['Symbol'] = 'ASX:'+ks['symbol'].split('.')[0]
            return params, 'Here is '+params['Symbol']
        else:
            return None, "We couldn't find that stock"

    @classmethod
    def get_google_html(cls, stock):
        html = requests.get('https://www.google.com/finance?q=ASX:' + stock)
        if html.status_code == 200:
            body = BeautifulSoup(html.text)
            if body.find(id='companyheader'):
                return body, 'Status code: '+html.status_code
            else:
                return None, "We couldn't find that stock"
        else:
            return None, 'Status code: '+html.status_code

    @classmethod
    def get_google_stats(cls, stock, params):
        body, msg = cls.get_google_html(stock)
        if body:
            params['Name'] = body.find(id='companyheader').h3.string
            params['Code'] = body.find(id='companyheader').div.next_sibling.a.string
            params['Price'] = body.find(id="price-panel").div.span.span.string

            element = body.find(attrs={"data-snapfield": 'eps'})
            params['EPS'] = element.parent.find(class_="val").string if element else ""
            element = body.find(attrs={"data-snapfield": 'pe_ratio'})
            params['PE'] = element.parent.find(class_="val").string if element else ""
            element = body.find(attrs={"data-snapfield": 'latest_dividend-dividend_yield'})
            params['DivYield'] = element.parent.find(class_="val").string if element else ""
            element = body.find(attrs={"data-snapfield": 'shares'})
            params['Shares'] = element.parent.find(class_="val").string if element else ""
            return params, 'Here is '+params['Code']
        else:
            return None, msg
