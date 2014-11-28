from google.appengine.ext import ndb

from core.models import BaseModel


class Stock(BaseModel):
    code = ndb.StringProperty(required=True)
    name = ndb.StringProperty()
    price = ndb.StringProperty()
    pe = ndb.StringProperty()
    price_sale = ndb.StringProperty()
    eps = ndb.StringProperty()
    total_cash_per_share = ndb.StringProperty()
    book_value_per_share = ndb.StringProperty()
    dividend_yield = ndb.StringProperty()
    profit_margin = ndb.StringProperty()
    total_debt = ndb.StringProperty()
    notes = ndb.StringProperty()
    shares = ndb.StringProperty()
    years_debt = ndb.StringProperty()
    # years_debt = ndb.ComputedProperty(lambda self: int(self.total_debt)*1000000/(int(self.eps)*int(self.shares)))

    @classmethod
    def get_by_code(cls, code):
        complete_code = 'ASX:'+code
        s = cls.query(cls.code == complete_code).get()
        if s:
            return s
        else:
            return None
