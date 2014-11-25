import endpoints

from api.controllers import StockEndpint

application = endpoints.api_server([StockEndpoint])