from api.helpers import BaseApiHelper
from api.messages import StockResponse

from core.models import Stock


class StockApiHelper(BaseApiHelper):
    """
    Class for creating the functions that help the controllers of the API.
    This one is specific for the model entity 'Stock'

    """
    _model = Stock

    def to_message(self, entity):
        """
        This function allows to prepare the entity for sending it
        through the API messages. Each Message Field is filled with
        its proper entity property.
        """
        return StockResponse(
            id=entity.key.id(),
            code=entity.code,
            companyName=entity.name,
            currentPrice=entity.price,
            pe=entity.pe,
            priceSales=entity.price_sale,
            eps=entity.eps,
            totalCashPerShare=entity.total_cash_per_share,
            bookValuePerShare=entity.book_value_per_share,
            dividendYield=entity.dividend_yield,
            profitMargin=entity.profit_margin,
            totalDebt=entity.total_debt,
            notes=entity.notes,
            yearsDebt=entity.years_debt,
            shares=entity.shares
            )
