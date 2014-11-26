from models.Stock import Stock
import yql_query
import google_finance

def query_put(stock):
	params={}
	params, msg = yql_query.get_stats(stock, params)

	#Put google_finance querys
	if params:
		s = Stock.get_by_code(stock)
		if s:						# Update the stats
			# First the yahoo stats
			s.PriceSales = params['PriceSales']
			s.TotalCashPerShare = params['TotalCashPerShare']
			s.BookValuePerShare = params['BookValuePerShare']
			s.ProfitMargin = params['ProfitMargin']
			s.TotalDebt = params['TotalDebt']
			# Google Stats

			s.put()					# Put it in the DataBase
		else:						# New Stock
			s = Stock(PriceSales = params['PriceSales'],
						TotalCashPerShare = params['TotalCashPerShare'],
						BookValuePerShare = params['BookValuePerShare'],
						ProfitMargin = params['ProfitMargin'],
						TotalDebt = params['TotalDebt'],
						code = params['Symbol'])
			s.put()
			return params['Symbol']+' has been added and updated'
	else:
		return msg