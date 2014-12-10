import json
import requests
from bs4 import BeautifulSoup

from core.models import Stock
from core.helpers import BaseHelper
from core.helpers.stock_helper import StockHelper


class QueryHelper(BaseHelper):
    """
    Class with all the methods created for querying the stocks
    information from Yahoo and Google Finance.

    """

    @classmethod
    def update_stock(cls, stock):
        """
        This method is for updating the information of an existing stock,
        in the database.

        """
        params = {}  # The dictionary is initialized
        stock_code = stock.code[4:]  # It removes the 'ASX:' from the code stored in the database, where is stored like 'ASX:###'.
        params1, msg_yahoo = cls.get_yahoo_stats(stock_code, params)  # Call the method for getting the stock stats from yahoo finance. params1 is the dictionary with the yahoo stats.
        params2, msg_google = cls.get_google_stats(stock_code, params)  # Call the method for getting the stock stats from google finance. params2 is the dictionary with the yahoo stats.

        if params1 or params2:  # It updates stats if the yahoo or the google query worked
            if params1:  # If the yahoo query worked
                params1 = StockHelper().convert_to_float(params1)  # Call this method for converting the stats that are in string format and can be converted to float format.
                stock.price_sale = params1['PriceSales']
                stock.total_cash_per_share = params1['TotalCashPerShare']
                stock.book_value_per_share = params1['BookValuePerShare']
                stock.profit_margin = params1['ProfitMargin']
                stock.total_debt = params1['TotalDebt']
                stock.code = params1['Symbol']
            if params2:  # If the google query worked
                params2 = StockHelper().convert_to_float(params2)  # Call this method for converting the stats that are in string format and can be converted to float format.
                stock.name = params2['Name']
                stock.price = params2['Price']
                stock.eps = params2['EPS']
                stock.pe = params2['PE']
                stock.dividend_yield = params2['DivYield']
                stock.shares = params2['Shares']
                stock.shares_num = params2['SharesNum']
            stock.years_debt = StockHelper().get_years_debt(params1, params2) if params1 and params2 else None  # If the Yahoo and the Google queries worked. So it's possible to calculate 'years_debt'
            stock.put()  # Saves it in the Database
            return [True, params['Symbol']+' has been updated']
        else:  # If both of the queries failed it returns a False and the error messages.
            return [False, msg_yahoo, msg_google]

    @classmethod
    def create_stock(cls, stock):
        """
        This method is for creating a new stock, and saving it
        in the database.

        """
        params = {}  # The dictionary is initialized
        params1, msg_yahoo = cls.get_yahoo_stats(stock, params)  # Call the method for getting the stock stats from yahoo finance.
        params2, msg_google = cls.get_google_stats(stock, params)  # Call the method for getting the stock stats from google finance.
        if params1 and params2:  # For creating a new stock both Yahoo and Google queries must work.
            params1 = StockHelper().convert_to_float(params1)  # Call this method for converting the stats that are in string format and can be converted to float format.
            params2 = StockHelper().convert_to_float(params2)  # Call this method for converting the stats that are in string format and can be converted to float format.
            new_stock = Stock(  # The new stock is created
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
            new_stock.put()  # Saves it in the Database
            return [True, new_stock, params['Symbol']+' has been created']
        else:  # If any of the queries failed it returns a False and the error messages.
            return [False, msg_yahoo, msg_google]

    @classmethod
    def get_yahoo_ks(cls, stock):
        """
        This method generates the query to yahoo finance. Using their YQL Endpoint.
        All the information is store in a JSON string.

        """
        # This is the URL of the yahoo API for quering a STOCK from ASX in JSON format.
        url = "http://query.yahooapis.com/v1/public/yql?q=SELECT%20*%20FROM%20yahoo.finance.keystats%20WHERE%20symbol%3D'{}.AX'&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=".format(stock)
        r = requests.get(url)  # Make the API request with the python library "requests".
        if not 'error' in json.loads(r.text):  # If the request fails, then the JSON contains an 'error' property
            ks = json.loads(r.text)['query']['results']['stats']  # The information needed is stored in 'stats'
            if 'MarketCap' in ks:  # If the stock doesn't exist so the JSON returned doesn't contain a 'MarketCap' property
                return ks
        return None

    @classmethod
    def get_yahoo_stats(cls, stock, params):
        """
        This method is for capturing the required properties from the JSON obtained in
        the method get_yahoo_ks().

        """
        ks = cls.get_yahoo_ks(stock)  # ks is the JSON obtained from making the query to the API of yahoo finance
        if ks:
            # The properties are in JSON properties. And they are obtained as a string.
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
        """
        This method generates the URL query to google finance.
        All the information is stored in the HTML of the webpage.
        The python library BeautifulSoup is helpful for scrapping the info from the HTML

        """
        # This is the URL the google finance. The code is send it as an URL parameter
        url = 'http://www.google.com/finance?q=ASX:{}'.format(stock)
        r = requests.get(url)  # Make the API request with the python library "requests".
        if r.status_code == 200:  # The HTTP status code allows to check if the request worked
            body = BeautifulSoup(r.text)  # The HTML string is converted into a BeautifulSoup Object that easies the scrapping of the code
            if body.find(id='companyheader'):  # If the stock exists so there is an html element with the id 'companyheader'
                return body, 'Status code: '+str(r.status_code)
            else:
                return None, "We couldn't find that stock"
        else:
            return None, 'Status code: '+r.status_code

    @classmethod
    def get_google_stats(cls, stock, params):
        """
        This method is for capturing the required properties from the BeautifulSoup Object
        created with the HTML obtained from the method get_google_html().
        """
        body, msg = cls.get_google_html(stock)  # body is the Object with the HTML from google Finance
        if body:
            # The properties from the Company Info are strings that are found next to certain HTML elements such a <h3>, <div>, <span>
            params['Name'] = body.find(id='companyheader').h3.string
            params['Code'] = body.find(id='companyheader').div.next_sibling.a.string
            params['Price'] = body.find(id="price-panel").div.span.span.string
            # The financial stats are strings wrapped by HTML elements which have 'data-snapfield' in the parent element and class='val' in the child.
            # The stats are obtained as a string with a '/n' character at the end that is dismissed.
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
