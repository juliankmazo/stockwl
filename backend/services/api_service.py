import endpoints

from api.controllers import StockEndpoint

application = endpoints.api_server([StockEndpoint])
