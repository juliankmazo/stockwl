import endpoints
from protorpc import messages
from protorpc import message_types

from stock_api_messages import StockRequest
from stock_api_messages import StockResponse
from stock_api_messages import StockListResponse

ID_resource = endpoints.ResourceContainer(
    message_types.VoidMessage,
    id=messages.IntegerField(1, variant=messages.Variant.INT64, required=True)
)
