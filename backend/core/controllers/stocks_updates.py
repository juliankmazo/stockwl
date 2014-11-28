from core.controllers import BaseController
from core.helpers import QueryHelper
from core.models import Stock


class UpdateStockController(BaseController):
    """
    Gets stats from yahoo and google, then updates the db
    """

    def get(self):
        stocks = Stock.query()
        if stocks:
            for s in stocks:
                QueryHelper().update_stock(s)
