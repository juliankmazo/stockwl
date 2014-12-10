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

    """
    Endpoint for retrieving all the stocks
    GET /stocks
    """
    @endpoints.method(message_types.VoidMessage, StockListResponse,
                      path='/stocks', http_method='GET',
                      name='find_all')
    def get_stocks(self, request):
        stocks = Stock.query().fetch()  # Query all stocks from the database
        return StockListResponse(stocks=[StockApiHelper().to_message(stock) for stock in stocks if stocks])  # Return the Message List Object with all the stocks

    """
    Endpoint for add a new stock to the list
    POST /stocks
    """
    @endpoints.method(StockRequest, StockListResponse,
                      path='/stocks', http_method='POST',
                      name='create')
    def create_stock(self, request):
        if not request.code:  # If there is no code in the request, raise a bad request error
            raise endpoints.BadRequestException('The variable code is needed')
        code = request.code.upper()  # Normalize the code string into uppercase string
        if Stock.get_by_code(code):  # Check if that specific code already exists, if it does it raises an exception
            raise endpoints.BadRequestException('This Stock already exists')
        status = QueryHelper().create_stock(code)  # Call the function to create the stock that it's in the QueryHelper class
        if status[0] is False:  # If the first argument of status is not True it's because something failed inside the function, so it shows the error messages in status [1] and [2]
            raise endpoints.NotFoundException('errors: ' + status[1] + ', ' + status[2])
        stock = status[1]  # The create_stock function succeed and the entity is in status[1]
        return StockListResponse(stocks=[StockApiHelper().to_message(stock)])  # Return the Message List Object with only the stock created

    """
    Endpoint for updating the property notes from one stock using its ID
    PUT /stocks/{id}
    """
    @endpoints.method(ID_resource, StockListResponse,
                      path='{id}', http_method='PUT',
                      name='update')
    def update_stock(self, request):
        stock = Stock.get_by_id(request.id)  # Query the stock using its ID from the database
        if not stock:  # If the stock doesn't exist, raise an error
            raise endpoints.BadRequestException("That Stock ID doesn't exist")
        stock.notes = request.notes  # Updates the value of the field notes in the entity according what it received
        stock.put()  # Update the stock in the database
        return StockListResponse(stocks=[StockApiHelper().to_message(stock)])  # Return the Message List Object with only the stock created

    """
    Endpoint for deleting one stock using its ID
    DELETE /stocks/{id}
    """
    @endpoints.method(ID_resource, StockListResponse,
                      path='{id}', http_method='DELETE',
                      name='delete')
    def delete_stock(self, request):
        stock = Stock.get_by_id(request.id)  # Query the stock using its ID from the database
        if not stock:  # If the stock doesn't exist, raise an error
            raise endpoints.BadRequestException("That Stock ID doesn't exist")
        else:
            stock.key.delete()  # If the stock exists, it removes it from the database
        stocks = Stock.query().fetch()  # Query all stocks from the database
        return StockListResponse(stocks=[StockApiHelper().to_message(stock) for stock in stocks if stocks])  # Return the Message List Object with all the stocks
