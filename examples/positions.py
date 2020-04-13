from RobinhoodTrader import RobinhoodTrader

trader = RobinhoodTrader()
trader.login()

print("Position:")

positions = trader.get_positions()
first_position = positions[0]

print(first_position)

print("Position Account:")
print(first_position.account())

print("Position Instrument:")
print(first_position.instrument())
