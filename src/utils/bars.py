import time

class Bars:
    def __init__(self):
        pass

    def get_stock_bars(self, stock_name: str, qtt_candles: int, mt5):
        return mt5.copy_rates_from(stock_name, mt5.TIMEFRAME_M5, time.time(),
                                   qtt_candles)
