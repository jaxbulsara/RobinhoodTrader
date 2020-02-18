from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

allWatchlists = trader.getAllCryptoWatchlists()
print("All watchlists:")
trader.printData(allWatchlists)

watchlist = trader.getCryptoWatchlist("Default")
print("Single watchlist")
trader.printData(watchlist)
