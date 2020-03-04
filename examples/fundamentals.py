from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

print("Tesla Fundamentals:")
teslaInstrument = trader.getInstrumentBySymbol("TSLAA")
teslaFundamentals = trader.getFundamentalsByInstrument(teslaInstrument)
teslaFundamentals = trader.getFundamentalsBySymbol("TSLAA")
trader.printData(teslaFundamentals)
