from google.appengine.ext import ndb

from core.models import BaseModel


class Stock(BaseModel):
    code = ndb.StringProperty(required = True)

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
