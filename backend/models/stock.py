from google.appengine.ext import ndb

class stock(ndb.Model):
	symbol = ndb.StringProperty(required = True)
	created = ndb.DateTimeProperty(auto_now_add = True)

	PE = ndb.FloatProperty()
	PS = ndb.FloatProperty()
	EPS = ndb.FloatProperty()
	CHPS = ndb.FloatProperty()
	BVPS = ndb.FloatProperty()
	DividendYield = ndb.FloatProperty()
	NetProfitMargin = ndb.FloatProperty()
	Debt = ndb.FloatProperty()
	Notes = ndb.StringProperty()
	YtpoD = ndb.ComputedProperty(lambda self: self.Debt*1000000/(self.EPS*self.Shares))
	Shares = ndb.IntegerProperty()