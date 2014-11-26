from lib import requests
from bs4 import BeautifulSoup

stock = 'gmx'
keys = ['eps','pe_ratio','latest_dividend-dividend_yield', 'shares']

def gf_query(query_stock, query_keys=keys):
	r = requests.get('https://www.google.com/finance?q=ASX:'+query_stock)
	stocks = {}
	if r.status_code==200:
		body = BeautifulSoup(r.text)
		if body.find(id='companyheader'):
			stocks['name'] = body.find(id='companyheader').h3.string
			stocks['code'] = body.find(id='companyheader').div.next_sibling.a.string
			stocks['price'] = body.find(id="price-panel").div.span.span.string
			for key in query_keys:
				element = body.find(attrs={"data-snapfield": key})
				value = element.parent.find(class_="val").string if element else ""
				stocks[key] = value
				# try:
				# 	stocks[key] = float(value)
				# except:
				# 	if key == 'shares':
				# 		stocks[key] = float(value[:-3])*1e6
				# 	else:
				# 		stocks[key] = 'N/A'
	return stocks