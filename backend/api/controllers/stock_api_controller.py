import endpoints
from protorpc import message_types
from core.models import Stock

from api import stock_api
from api.messages import ID_resource
from api.messages import StockListResponse
from api.messages import StockRequest
from api.helpers import StockApiHelper
from api.controllers import BaseApiController

from core.helpers import QueryHelper


@stock_api.api_class(resource_name='stocks', path='stocks')
class StockEndpoint(BaseApiController):

    @endpoints.method(message_types.VoidMessage, StockListResponse,
                      path='/stocks', http_method='GET',
                      name='find_all')
    def get_stocks(self, request):
        stocks = Stock.query().fetch()
        return StockListResponse(stocks=[StockApiHelper().to_message(stock) for stock in stocks if stocks])

    @endpoints.method(ID_resource, StockListResponse,
                      path='{id}', http_method='DELETE',
                      name='delete')
    def update_stock(self, request):
        stock = Stock.get_by_id(request.id)
        if not stock:
            raise endpoints.BadRequestException("That Stock ID doesn't exist")
        else:
            stock.key.delete()
        stocks = Stock.query().fetch()
        return StockListResponse(stocks=[StockApiHelper().to_message(stock) for stock in stocks if stocks])

    @endpoints.method(StockRequest, StockListResponse,
                      path='/stocks', http_method='POST',
                      name='create')
    def create_stock(self, request):
        if not request.code:
            raise endpoints.BadRequestException('The variable code is needed')
        else:
            code = request.code.upper()
        if Stock.get_by_code(code):
            raise endpoints.BadRequestException('This Stock already exists')
        status = QueryHelper().create_stock(code)
        if status[0] is False:
            raise endpoints.NotFoundException('errors: ' + status[1] + ', ' + status[2])
        stock = status[1]
        return StockListResponse(stocks=[StockApiHelper().to_message(stock)])

    @endpoints.method(ID_resource, StockListResponse,
                      path='{id}', http_method='PUT',
                      name='update')
    def delete_stock(self, request):
        stock = Stock.get_by_id(request.id)
        if not stock:
            raise endpoints.BadRequestException("That Stock ID doesn't exist")
        stock.notes = request.notes
        stock.put()
        return StockListResponse(stocks=[StockApiHelper().to_message(stock)])
