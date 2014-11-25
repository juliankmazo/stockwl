from protorpc import messages
from protorpc import message_types

from stock_api_messages import StockRequest
from stock_api_messages import StockResponse

BaseResourceContainer = endpoints.ResourceContainer(
        message_types.VoidMessage,
        id=messages.IntegerField(2, variant=messages.Variant.INT64, required=True)
)