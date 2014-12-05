from google.appengine.ext import ndb

from core.models import BaseModel


class Stock(BaseModel):
    code = ndb.StringProperty(required=True)
    name = ndb.StringProperty()
    price = ndb.FloatProperty()
    pe = ndb.FloatProperty()
    price_sale = ndb.FloatProperty()
    eps = ndb.FloatProperty()
    total_cash_per_share = ndb.FloatProperty()
    book_value_per_share = ndb.FloatProperty()
    dividend_yield = ndb.FloatProperty()
    profit_margin = ndb.FloatProperty()
    total_debt = ndb.FloatProperty()
    notes = ndb.StringProperty()
    shares = ndb.StringProperty()
    shares_num = ndb.FloatProperty()
    years_debt = ndb.FloatProperty()

    @classmethod
    def get_by_code(cls, code):
        complete_code = 'ASX:'+code
        s = cls.query(cls.code == complete_code).get()
        if s:
            return s
        else:
            return None
