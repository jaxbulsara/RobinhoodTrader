from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
# trader.login()

currencyPairPage = trader.getFirstCurrencyPairPage()
trader.printData(currencyPairPage)
