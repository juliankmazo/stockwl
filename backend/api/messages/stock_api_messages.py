from protorpc import messages


# Message Model for the Stock Information of the API responses
class StockResponse(messages.Message):
    id = messages.IntegerField(1)
    code = messages.StringField(2)
    companyName = messages.StringField(3)
    currentPrice = messages.FloatField(4)
    pe = messages.FloatField(5)
    priceSales = messages.FloatField(6)
    eps = messages.FloatField(7)
    totalCashPerShare = messages.FloatField(8)
    bookValuePerShare = messages.FloatField(9)
    dividendYield = messages.FloatField(10)
    profitMargin = messages.FloatField(11)
    totalDebt = messages.FloatField(12)
    notes = messages.StringField(13)
    yearsDebt = messages.FloatField(14)
    shares = messages.StringField(15)


# Message Model for the arguments needed for the UPDATE Endpoint
class StockEditNoteRequest(messages.Message):
    notes = messages.StringField(1)


# Message Model for creating a List of StockResponse Message Class for the API responses
class StockListResponse(messages.Message):
    stocks = messages.MessageField(StockResponse, 1, repeated=True)
    count = messages.IntegerField(2)


# Message Model for the request of creating a new stock where the field 'code' is needed
class StockRequest(messages.Message):
    code = messages.StringField(1, required=True)
