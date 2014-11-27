import endpoints

from api import stock_api
from api.messages import ID_resource
from api.messages import StockResponse
# from messages import StockRequest

from api.controllers import BaseApiController


@stock_api.api_class(resource_name='stocks', path='stocks')
class StockEndpoint(BaseApiController):

    @endpoints.method(ID_resource, StockResponse,
                      path='', http_method='GET',
                      name='find_all')
    def get_stocks(self, request):
        code = 'code:'+str(request.id)
        return StockResponse(code=code, message='OK')

    @endpoints.method(ID_resource, StockResponse,
                      path='{id}', http_method='PUT',
                      name='update')
    def update_stock(self, request):
        code = 'code:'+str(request.id)
        return StockResponse(code=code, message='OK')

    @endpoints.method(ID_resource, StockResponse,
                      path='', http_method='POST',
                      name='create')
    def create_stock(self, request):
        code = 'code:'+str(request.id)
        return StockResponse(code=code, message='OK')

    @endpoints.method(ID_resource, StockResponse,
                      path='{id}', http_method='DELETE',
                      name='delete')
    def delete_stock(self, request):
        code = 'code:'+str(request.id)
        return StockResponse(code=code, message='OK')
