from protorpc import messages


class StockResponse(messages.Message):
    id = messages.IntegerField(1)
    code = messages.StringField(2)
    companyName = messages.StringField(3)
    currentPrice = messages.StringField(4)
    pe = messages.StringField(5)
    priceSales = messages.StringField(6)
    eps = messages.StringField(7)
    totalCashPerShare = messages.StringField(8)
    bookValuePerShare = messages.StringField(9)
    dividendYield = messages.StringField(10)
    profitMargin = messages.StringField(11)
    totalDebt = messages.StringField(12)
    notes = messages.StringField(13)
    yearsDebt = messages.StringField(14)
    shares = messages.StringField(15)


class StockEditNoteRequest(messages.Message):
    id = messages.IntegerField(1)
    notes = messages.StringField(2)


class StockListResponse(messages.Message):
    stocks = messages.MessageField(StockResponse, 1, repeated=True)
    count = messages.IntegerField(2)


class StockRequest(messages.Message):
    code = messages.StringField(1, required=True)
