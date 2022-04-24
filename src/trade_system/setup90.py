from src.indicators import Indicators

class Setup90():
    def __init__(self):
        return
    
    def __get_indicators(self, prices, stock_name):
        indicators = Indicators()
        self._ema9 = indicators.simple_moving_average(prices, stock_name, 9)
        self._ema21 = indicators.simple_moving_average(prices, stock_name, 21)

    def run(self, stock_name, prices):
        self.__get_indicators(prices, stock_name)