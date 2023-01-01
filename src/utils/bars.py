import time


class Bars:
    def __init__(self, mt5):
        self.mt5 = mt5
        pass

    def get_stock_bars(self, stock_name: str, qtt_candles: int, timeframe):
        return self.mt5.copy_rates_from(stock_name, timeframe, time.time(),
                                        qtt_candles)
