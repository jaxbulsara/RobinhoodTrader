from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

allWatchlists = trader.cryptoBroker.getAllWatchlists()
print("All watchlists:")
trader.printData(allWatchlists)

watchlist = trader.cryptoBroker.getWatchlist("Default")
print("Single watchlist")
trader.printData(watchlist)
