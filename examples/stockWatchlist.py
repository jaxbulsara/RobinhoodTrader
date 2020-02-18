from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

allWatchlists = trader.getAllWatchlists()
print("All watchlists:")
trader.printData(allWatchlists)

watchlist = trader.getWatchlist("Default")
print("Single watchlist")
trader.printData(watchlist)
