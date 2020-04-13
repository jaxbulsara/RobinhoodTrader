from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

print("Tesla Fundamentals:")

tesla = trader.get_instrument("TSLA")
tesla_fundamentals = tesla.fundamentals()
tesla_fundamentals = trader.get_fundamentals(tesla)
tesla_fundamentals = trader.get_fundamentals("TSLA")

print(tesla_fundamentals)
