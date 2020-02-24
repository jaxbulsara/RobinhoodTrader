from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

watchlist = trader.getWatchlist()
trader.printData(watchlist)

instruments = trader.getWatchlistInstruments(watchlist)
trader.printData(instruments)

sampleInstrument = instruments[0]
deleteResponse = trader.deleteFromWatchlist(sampleInstrument)
print(deleteResponse)

addResponse = trader.addToWatchlist(sampleInstrument)
trader.printData(addResponse)

sampleInstruments = instruments[0:3]
deleteMultipleResponse = trader.deleteMultipleFromWatchlist(sampleInstruments)
trader.printData(deleteMultipleResponse)

addMultipleResponse = trader.addMultipleToWatchlist(sampleInstruments)
trader.printData(addMultipleResponse)
