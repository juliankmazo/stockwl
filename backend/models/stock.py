from google.appengine.ext import ndb

class Stock(ndb.Model):
	code = ndb.StringProperty(required = True)
	created = ndb.DateTimeProperty(auto_now_add = True)

	PE = ndb.StringProperty()
	PriceSales = ndb.StringProperty()
	EPS = ndb.StringProperty()
	TotalCashPerShare = ndb.StringProperty()
	BookValuePerShare = ndb.StringProperty()
	DividendYield = ndb.StringProperty()
	ProfitMargin = ndb.StringProperty()
	TotalDebt = ndb.StringProperty()
	Notes = ndb.StringProperty()
	YearsDebt = ndb.ComputedProperty(lambda self: self.Debt*1000000/(self.EPS*self.Shares))
	Shares = ndb.IntegerProperty()

	@classmethod
	def get_by_code(cls, code):
		complete_code = 'ASX:'+code
		s = cls.query(cls.code == complete_code).get()
		if s:
			return s
		else:
			return None
