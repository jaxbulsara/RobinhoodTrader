from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

print("Bitcoin Currency Pair:")
bitcoin = trader.getCurrencyPairBySymbol("BTC-USD")
bitcoin = trader.getCurrencyPairById(bitcoin["id"])
trader.printData(bitcoin)
