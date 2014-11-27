import endpoints

from api.controllers import StockEndpoint

APPLICATION = endpoints.api_server([StockEndpoint])
