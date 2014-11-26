import requests
import json

def get_ks(stock):
	url = "https://query.yahooapis.com/v1/public/yql?q=SELECT%20*%20FROM%20yahoo.finance.keystats%20WHERE%20symbol%3D'{}.AX'&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=".format(stock)
	r = requests.get(url)
	ks = json.loads(r.text)['query']['results']['stats']
	if 'MarketCap' in ks:
		return ks
	else:
		return None

def get_stats(stock, params):
	ks = get_ks(stock)
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
