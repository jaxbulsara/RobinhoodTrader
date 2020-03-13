from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

print("Account:")
account = trader.get_account()
print(account)

