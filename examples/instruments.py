from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

print("Tesla Instrument:")

# by symbol
teslaInstrument = trader.getInstrument("TSLA")

# by instrument id
teslaInstrument = trader.getInstrument(teslaInstrument["id"])

# by instrument url
teslaInstrument = trader.getInstrument(teslaInstrument["url"])

trader.printData(teslaInstrument)

