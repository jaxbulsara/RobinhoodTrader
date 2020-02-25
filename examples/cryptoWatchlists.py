from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

print("Crypto Watchlist:")
cryptoWatchlist = trader.getCryptoWatchlist()
trader.printData(cryptoWatchlist)

print("Crypto Watchlist Currency Pairs:")
watchlistCurrencyPairs = trader.getCryptoWatchlistCurrencyPairs(cryptoWatchlist)
trader.printData(watchlistCurrencyPairs)
