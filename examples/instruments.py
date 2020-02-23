from RobinhoodTrader import RobinhoodTrader
import pprint

trader = RobinhoodTrader()
trader.login()

allInstruments = trader.getAllInstruments()
with open("allInstruments.txt", "w") as instrumentFile:
    pprint.pprint(allInstruments, instrumentFile, indent=4)



