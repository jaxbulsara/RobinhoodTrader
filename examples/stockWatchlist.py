from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

allWatchlists = trader.stockBroker.getAllWatchlists()
print("All watchlists:")
trader.printData(allWatchlists)

watchlist = trader.stockBroker.getWatchlist("Default")
print("Single watchlist")
trader.printData(watchlist)
