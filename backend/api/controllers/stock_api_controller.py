import endpoints

from messages import BaseResourceContainer
from messages import StockResponse



@stock_api.api_class(resource_name='stocks', path='stocks')
	class StockEndpoint(remote.Service):
		
		@endpoints.method(BaseResourceContainer, StockResponse,
			path='{id}',	http_method='GET',
			name='stocks.get')
		def get_stock(self, request):
			pass
