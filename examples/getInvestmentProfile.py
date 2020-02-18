from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

investmentProfile = trader.getInvestmentProfile()
print("Investment Profile:")
trader.printData(investmentProfile)
