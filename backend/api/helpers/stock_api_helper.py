from api.helpers import BaseApiHelper
from api.messages import StockResponse

from core.models import Stock


class StockApiHelper(BaseApiHelper):

    _model = Stock

    def to_message(self, entity):
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
