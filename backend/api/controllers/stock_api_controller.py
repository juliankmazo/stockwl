import endpoints
from protorpc import remote

import stock_api
from messages import BaseResourceContainer
from messages import StockResponse


@stock_api.api_class(resource_name='stocks', path='stocks')
class StockEndpoint(remote.Service):

        @endpoints.method(BaseResourceContainer, StockResponse,
                          path='{id}', http_method='GET',
                          name='stocks.get')
        def get_stock(self, request):
            code = request.code
            return StockResponse(code=code, message='OK')
