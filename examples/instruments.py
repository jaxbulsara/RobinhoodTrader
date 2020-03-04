from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

print("Tesla Instrument:")
teslaInstrument = trader.getInstrumentBySymbol("TSLA")
teslaInstrument = trader.getInstrumentById(teslaInstrument["id"])
teslaInstrument = trader.getInstrumentByUrl(teslaInstrument["url"])
trader.printData(teslaInstrument)

