from google.appengine.ext import ndb

from core.models import BaseModel


class Stock(BaseModel):
    code = ndb.StringProperty(required=True)

    pe = ndb.StringProperty()
    price_sales = ndb.StringProperty()
    eps = ndb.StringProperty()
    total_cash_per_share = ndb.StringProperty()
    book_value_per_share = ndb.StringProperty()
    dividend_yield = ndb.StringProperty()
    profit_margin = ndb.StringProperty()
    total_debt = ndb.StringProperty()
    notes = ndb.StringProperty()
    years_debt = ndb.ComputedProperty(lambda self: self.Debt*1000000/(self.EPS*self.Shares))
    shares = ndb.IntegerProperty()

    @classmethod
    def get_by_code(cls, code):
        complete_code = 'ASX:'+code
        s = cls.query(cls.code == complete_code).get()
        if s:
            return s
        else:
            return None
