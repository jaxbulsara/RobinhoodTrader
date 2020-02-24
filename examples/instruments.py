from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

print("Tesla Instrument:")
teslaInstrument = trader.getInstrumentBySymbol("TSLA")
teslaInstrument = trader.getInstrumentById(teslaInstrument["id"])
teslaInstrument = trader.getInstrumentByUrl(teslaInstrument["url"])
trader.printData(teslaInstrument)

print("Tesla Fundamentals:")
teslaFundamentals = trader.getFundamentalsByInstrument(teslaInstrument)
teslaFundamentals = trader.getFundamentalsBySymbol("TSLA")
trader.printData(teslaFundamentals)

print("Tesla Quote:")
teslaQuote = trader.getQuoteByInstrument(teslaInstrument)
teslaQuote = trader.getQuoteBySymbol("TSLA")
trader.printData(teslaQuote)

print("Tesla Market:")
teslaMarket = trader.getMarketByInstrument(teslaInstrument)
trader.printData(teslaMarket)
