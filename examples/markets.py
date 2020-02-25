from RobinhoodTrader import RobinhoodTrader
import datetime

trader = RobinhoodTrader()
trader.login()

print("All Markets:")
markets = trader.getFirstMarketPage()
trader.printData(markets)

print("New York Stock Exchange")
nyse = trader.getMarketByIdentifierCode("XNYS")
trader.printData(nyse)

print("Market that Tesla is listed in:")
tesla = trader.getInstrumentBySymbol("TSLA")
teslaMarket = trader.getMarketByInstrument(tesla)
trader.printData(teslaMarket)

print("Today's NYSE Hours:")
nyseHours = trader.getMarketHours(nyse)
trader.printData(nyseHours)

print("Tomorrow's NYSE Hours:")
nyseNextDayHours = trader.getMarketNextDayHours(nyse)
trader.printData(nyseNextDayHours)

print("Get NYSE Hours on March 3, 2050:")
marketDate = datetime.date(2050, 3, 3)
nyseHoursByDate = trader.getMarketHoursByDate(nyse, marketDate)
trader.printData(nyseHoursByDate)
