from core.helpers import BaseHelper
from core.models import Stock


class StockHelper(BaseHelper):

    @classmethod
    def convert_to_float2(cls, stock):
        for stat in Stock._properties:
            if stat in ['price', 'pe', 'eps', 'price_sales', 'total_cash_per_share', 'book_value_per_share', 'total_debt', 'profit_margin']:
                value = getattr(stock, stat)
                try:
                    new_value = float(value)
                except:
                    new_value = float('NaN')
                setattr(stock, stat, new_value)

    @classmethod
    def convert_to_float(cls, params):
        for stat in params:
            if stat in ['Price', 'PE', 'EPS', 'PriceSales', 'TotalCashPerShare', 'BookValuePerShare', 'TotalDebt', 'ProfitMargin']:
                value = params[stat]
                try:
                    new_value = float(value)
                except:
                    new_value = None
                params[stat] = new_value
        value = params['Shares']
        if value[-1] == 'K':
            new_value = float(value[:-1])*10e3
        elif value[-1] == 'M':
            new_value = float(value[:-1])*10e6
        elif value[-1] == 'B':
            new_value = float(value[:-1])*10e9
        else:
            try:
                new_value = float(value)
            except:
                new_value = None
        params['SharesNum'] = new_value
        return params

    @classmethod
    def get_years_debt(cls, params1, params2):
        if params1['TotalDebt'] and params2['EPS'] and params2['SharesNum']:
            return params1['TotalDebt']*1000000/(params2['EPS']*params2['SharesNum'])
        return None
