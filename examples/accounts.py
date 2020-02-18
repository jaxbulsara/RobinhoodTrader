from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

allStockAccounts = trader.getAllAccounts()
print("\nAll stock accounts:")
trader.printData(allStockAccounts)

allCryptoAccounts = trader.getAllCryptoWatchlists()
print("\nAll crypto accounts:")
trader.printData(allCryptoAccounts)

stockAccount = trader.getAccount()
print("\nDefault stock account:")
trader.printData(stockAccount)

cryptoAccount = trader.getCryptoAccount()
print("\nDefault crypto account:")
trader.printData(cryptoAccount)
