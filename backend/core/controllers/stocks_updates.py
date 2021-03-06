from core.controllers import BaseController
from core.helpers import QueryHelper
from core.models import Stock

import logging


class UpdateStockController(BaseController):
    """
    This function is the one that is run periocally.
    It updates the stock information.
    Gets stats from yahoo and google, then updates the database.
    """

    def get(self):
        stocks = Stock.query()
        if stocks:
            for s in stocks:
                status = QueryHelper().update_stock(s)
                if status[0]:
                    logging.info(status[1])
