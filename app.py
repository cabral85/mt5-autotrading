import MetaTrader5 as mt5

from src.setup.setup_90 import Setup90
from src.utils.contracts import Contracts

contracts = Contracts()
stocks = contracts.get_stocks()
stocks.extend(contracts.get_future_contracts())

if not mt5.initialize():
        print("mt5 initialize() failed")
        mt5.shutdown()

print(mt5.terminal_info())
print(mt5.version())


setup = Setup90("WINM22", mt5)
setup.run()