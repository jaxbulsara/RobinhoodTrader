from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

investmentProfile = trader.stockBroker.getInvestmentProfile()
print("Investment Profile:")
trader.printData(investmentProfile)
