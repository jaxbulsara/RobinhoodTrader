from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

print("Tesla Quote:")
tesla = trader.get_instrument("TSLA")

tesla_quote = tesla.quote()
tesla_quote = trader.get_quote(tesla)
tesla_quote = trader.get_quote(tesla.id)
tesla_quote = trader.get_quote("TSLA")

print(tesla_quote)
