from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

print("Account:")
trader.printData(trader.getCryptoAccount())

print("Positions:")
trader.printData(trader.getCryptoHoldings())
