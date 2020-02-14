# logs into robinhood

from Robinhood.Robinhood.Robinhood import Robinhood

QR = "4SMM5FRDEASR7W6Y"
trader = Robinhood()
login = trader.login(username="jaxbulsara@gmail.com", password="Relatr4bivity", qr_code=QR)
quote_info = trader.quote_data("BTC")
print(quote_info)