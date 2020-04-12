from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

print("Tesla Fundamentals:")

tesla = trader.get_instrument("TSLA")

tesla_fundamentals = trader.get_fundamentals(tesla)

print(tesla_fundamentals)
