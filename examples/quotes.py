from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

print("Tesla Quote:")
teslaInstrument = trader.getInstrumentBySymbol("TSLA")
teslaQuote = trader.getQuoteByInstrument(teslaInstrument)
teslaQuote = trader.getQuoteBySymbol("TSLA")
trader.printData(teslaQuote)
