from indicators import Indicators
from src.trade_system.setup_interface import SetupInterface

class Setup92(SetupInterface):
    def __init__(self):
        return
    
    def __get_indicators(self, prices):
        indicators = Indicators()
        self._ema9 = indicators.exponential_moving_average(self._futures_prices, 9)
        self._ema21 = indicators.exponential_moving_average(self._futures_prices, 21)

    def run(self, stock_name, prices):
        return