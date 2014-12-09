import endpoints
from protorpc import messages
from protorpc import message_types

from stock_api_messages import StockRequest
from stock_api_messages import StockResponse
from stock_api_messages import StockListResponse
from stock_api_messages import StockEditNoteRequest

ID_resource = endpoints.ResourceContainer(
    StockEditNoteRequest,
    id=messages.IntegerField(1, variant=messages.Variant.INT64, required=True)
)
