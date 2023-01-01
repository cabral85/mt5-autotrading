from datetime import datetime
from time import sleep
import MetaTrader5 as mt5

from src.setup.setup_90 import Setup90
from src.utils.contracts import get_stocks, get_future_contracts

stocks = get_stocks()
stocks.extend(get_future_contracts())

if not mt5.initialize():
    print("mt5 initialize() failed")
    mt5.shutdown()

print(mt5.terminal_info())
print(mt5.version())

while True:
    for stock in stocks:
        setup = Setup90(mt5)
        setup.run(stock)
    sleep_time = 60 - datetime.utcnow().second
    sleep(sleep_time)
