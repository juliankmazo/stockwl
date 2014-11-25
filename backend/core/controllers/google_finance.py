from lib import requests
from bs4 import BeautifulSoup

# from models.stock import Stock
query_stock = 'gmx.ax'
query_keys = ['eps', 'shares', 'pe_ratio']

def gf_query(query_stock, query_keys=[]):

	r = requests.get('https://www.google.com/finance?q=' + query_stock)
	if r.status_code==200:
		body = BeautifulSoup(r.text)
		for key in query_keys:
			element = body.find(attrs={"data-snapfield": key})
			print element
			value = element.parent.find(class_="val").string if element else ""
			print  u'{key}: {value}'.format(key=key, value=value)