from core.helpers import BaseHelper


class StockHelper(BaseHelper):
    """
    Class with the methods created to help format the property of the stocks.
    """

    @classmethod
    def convert_to_float(cls, params):
        """
        Method for formatting the stats than can be converted to float.
        """
        for stat in params:
            # Some stats can be converted directly
            if stat in ['Price', 'PE', 'EPS', 'PriceSales', 'TotalCashPerShare', 'BookValuePerShare', 'TotalDebt', 'ProfitMargin']:
                value = params[stat]
                try:
                    new_value = float(value)
                except:
                    new_value = None
                params[stat] = new_value
        if 'DivYield' in params:  # The DivYield stat is obtained taking the denominator of the fraction
            value = params['DivYield']
            if isinstance(value, basestring):
                try:
                    new_value = float(value.split('/')[1])
                except:
                    new_value = None
                params['DivYield'] = new_value
        if 'Shares' in params:   # The number of shares are needed to calculate the years_debt. So it's necessary to remove the letter of the 10th power and multiply it by the correct factor.
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
        """
        Method for calculating the years_debt property.
        """
        if params1['TotalDebt'] and params2['EPS'] and params2['SharesNum']:
            return round(params1['TotalDebt']/(params2['EPS']*params2['SharesNum']), 2)
        return None
