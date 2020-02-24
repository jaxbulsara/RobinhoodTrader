from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

print("Account:")
trader.printData(trader.getAccount())

print("Positions:")
trader.printData(trader.getPositions())
