import json
import requests
# import google_finance

from models.Stock import Stock
from core.helpers import BaseHelper


class QueryHelper(BaseHelper):

    @classmethod
    def query_put(cls, stock):
        params = {}
        params, msg = cls.get_yahoo_stats(stock, params)

        #Put google_finance querys
        if params:
            s = Stock.get_by_code(stock)
            if s:                       # Update the stats
                # First the yahoo stats
                s.price_sale = params['PriceSales']
                s.total_cash_per_share = params['TotalCashPerShare']
                s.book_value_per_share = params['BookValuePerShare']
                s.profit_margin = params['ProfitMargin']
                s.total_debt = params['TotalDebt']
                # Google Stats

                s.put()                 # Put it in the DataBase
            else:                       # New Stock
                s = Stock(
                    price_sale=params['PriceSales'],
                    total_cash_per_share=params['TotalCashPerShare'],
                    book_value_per_share=params['BookValuePerShare'],
                    profit_margin=params['ProfitMargin'],
                    total_debt=params['TotalDebt'],
                    code=params['Symbol']
                    #Google stats
                )
                s.put()
                return params['Symbol']+' has been added and updated'
        else:
            return msg

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
        ks = cls.get_yahoo_ks(stock)
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
