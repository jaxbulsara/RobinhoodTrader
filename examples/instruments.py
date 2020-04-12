from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

print("Tesla Instrument:")

# by symbol
tesla = trader.get_instrument("TSLA")

# by instrument id
tesla = trader.get_instrument(tesla.id)

# by instrument url
tesla = trader.get_instrument(tesla.url)

print(tesla)

