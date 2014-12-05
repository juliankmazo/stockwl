import json
import logging
import requests
from bs4 import BeautifulSoup

from core.models import Stock
from core.helpers import BaseHelper
from core.helpers.stock_helper import StockHelper


class QueryHelper(BaseHelper):

    @classmethod
    def update_stock(cls, stock):
        params = {}
        stock_code = stock.code[4:]
        params1, msg_yahoo = cls.get_yahoo_stats(stock_code, params)
        params2, msg_google = cls.get_google_stats(stock_code, params)

        if params1 or params2:
            if params1:
                # The yahoo stats
                params1 = StockHelper().convert_to_float(params1)
                stock.price_sale = params1['PriceSales']
                stock.total_cash_per_share = params1['TotalCashPerShare']
                stock.book_value_per_share = params1['BookValuePerShare']
                stock.profit_margin = params1['ProfitMargin']
                stock.total_debt = params1['TotalDebt']
                stock.code = params1['Symbol']
            if params2:
                # The google Stats
                params2 = StockHelper().convert_to_float(params2)
                stock.name = params2['Name']
                stock.price = params2['Price']
                stock.eps = params2['EPS']
                stock.pe = params2['PE']
                stock.dividend_yield = params2['DivYield']
                stock.shares = params2['Shares']
                stock.shares_num = params2['SharesNum']
            # Put it in the DataBase
            stock.years_debt = StockHelper().get_years_debt(params1, params2) if params1 and params2 else None
            stock.put()
            return [True, params['Symbol']+' has been updated']
        else:
            return [False, msg_yahoo, msg_google]

    @classmethod
    def create_stock(cls, stock):
        params = {}
        params1, msg_yahoo = cls.get_yahoo_stats(stock, params)
        params2, msg_google = cls.get_google_stats(stock, params)
        logging.error('PAR1 ANTES')
        logging.error(params1)
        logging.error('PAR2 ANTES')
        logging.error(params2)
        if params1 and params2:
            params1 = StockHelper().convert_to_float(params1)
            params2 = StockHelper().convert_to_float(params2)
            logging.error('PAR1')
            logging.error(params1)
            logging.error('PAR2')
            logging.error(params2)
            new_stock = Stock(
                price_sale=params1['PriceSales'],
                total_cash_per_share=params1['TotalCashPerShare'],
                book_value_per_share=params1['BookValuePerShare'],
                profit_margin=params1['ProfitMargin'],
                total_debt=params1['TotalDebt'],
                code=params1['Symbol'],
                name=params2['Name'],
                price=params2['Price'],
                eps=params2['EPS'],
                pe=params2['PE'],
                dividend_yield=params2['DivYield'],
                shares=params2['Shares'],
                shares_num=params2['SharesNum'],
                years_debt=StockHelper().get_years_debt(params1, params2)
            )
            new_stock.put()
            return [True, params['Symbol']+' has been created']
        else:
            return [False, msg_yahoo, msg_google]

    @classmethod
    def get_yahoo_ks(cls, stock):
        url = "http://query.yahooapis.com/v1/public/yql?q=SELECT%20*%20FROM%20yahoo.finance.keystats%20WHERE%20symbol%3D'{}.AX'&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=".format(stock)
        r = requests.get(url)
        if not 'error' in json.loads(r.text):
            ks = json.loads(r.text)['query']['results']['stats']
            if 'MarketCap' in ks:
                return ks
        return None

    @classmethod
    def get_yahoo_stats(cls, stock, params):
        ks = cls.get_yahoo_ks(stock)
        if ks:
            params['PriceSales'] = ks['PriceSales']['content']
            params['TotalCashPerShare'] = ks['TotalCashPerShare']['content']
            params['BookValuePerShare'] = ks['BookValuePerShare']['content']
            params['ProfitMargin'] = ks['ProfitMargin']['content'][:-1]
            params['TotalDebt'] = ks['TotalDebt']['content'] if 'content' in ks['TotalDebt'] else 'N/A'
            params['Symbol'] = 'ASX:'+ks['symbol'].split('.')[0]
            return params, 'Here is '+params['Symbol']
        else:
            return None, "We couldn't find that stock"

    @classmethod
    def get_google_html(cls, stock):
        url = 'http://www.google.com/finance?q=ASX:{}'.format(stock)
        r = requests.get(url)
        if r.status_code == 200:
            body = BeautifulSoup(r.text)
            if body.find(id='companyheader'):
                return body, 'Status code: '+str(r.status_code)
            else:
                return None, "We couldn't find that stock"
        else:
            return None, 'Status code: '+r.status_code

    @classmethod
    def get_google_stats(cls, stock, params):
        body, msg = cls.get_google_html(stock)
        if body:
            params['Name'] = body.find(id='companyheader').h3.string
            params['Code'] = body.find(id='companyheader').div.next_sibling.a.string
            params['Price'] = body.find(id="price-panel").div.span.span.string

            element = body.find(attrs={"data-snapfield": 'eps'})
            params['EPS'] = element.parent.find(class_="val").string[:-1] if element else ""
            element = body.find(attrs={"data-snapfield": 'pe_ratio'})
            params['PE'] = element.parent.find(class_="val").string[:-1] if element else ""
            element = body.find(attrs={"data-snapfield": 'latest_dividend-dividend_yield'})
            params['DivYield'] = element.parent.find(class_="val").string[:-1] if element else ""
            element = body.find(attrs={"data-snapfield": 'shares'})
            params['Shares'] = element.parent.find(class_="val").string[:-1] if element else ""
            return params, 'Here is '+params['Code']
        else:
            return None, msg
