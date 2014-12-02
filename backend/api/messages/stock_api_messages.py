from protorpc import messages


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
    dividendYield = messages.StringField(10)
    profitMargin = messages.FloatField(11)
    totalDebt = messages.FloatField(12)
    notes = messages.StringField(13)
    yearsDebt = messages.FloatField(14)
    shares = messages.StringField(15)


class StockEditNoteRequest(messages.Message):
    id = messages.IntegerField(1)
    notes = messages.StringField(2)


class StockListResponse(messages.Message):
    stocks = messages.MessageField(StockResponse, 1, repeated=True)
    count = messages.IntegerField(2)


class StockRequest(messages.Message):
    code = messages.StringField(1, required=True)
