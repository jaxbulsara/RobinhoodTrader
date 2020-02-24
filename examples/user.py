from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

print("User:")
trader.printData(trader.getUser())

print("Basic Info:")
trader.printData(trader.getUserBasicInfo())

print("Additional Info:")
trader.printData(trader.getUserAdditionalInfo())

print("CIP Questions:")
trader.printData(trader.getUserCipQuestions())

print("Employment:")
trader.printData(trader.getUserEmployment())

print("Identity Mismatch:")
trader.printData(trader.getUserIdentityMismatch())

print("Investment Profile:")
trader.printData(trader.getUserInvestmentProfile())
