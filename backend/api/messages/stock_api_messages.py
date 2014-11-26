from protorpc import messages


class StockResponse(messages.Message):
    code = messages.StringField(1)
    message = messages.StringField(2)


class StockRequest(messages.Message):
    code = messages.StringField(1, required=True)
