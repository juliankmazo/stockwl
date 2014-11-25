from protorpc import messages


class StockResponse(messages.Message):
	name = messages.StringField(1)

class StockRequest(messages.Message):
	name = messages.StringField(1)