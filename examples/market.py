from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

print("Microsoft's Market:")

microsoft = trader.get_instrument("MSFT")
print(microsoft.market())

print("Market by MIC:")
print(trader.get_market("XNAS"))

print("XNAS hours")
print(microsoft.market.hours())
