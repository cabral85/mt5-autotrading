import MetaTrader5 as mt5
from datetime import datetime


class Bars:
    def __init__(self):
        self.__create_connection()

    def __create_connection(self):
        if not mt5.initialize():
            print("mt5 initialize() failed")
            mt5.shutdown()

        print(mt5.terminal_info())
        print(mt5.version())

    def get_stock_bars(self, stock_name: str, qtt_candles: int):
        today = datetime.today()
        return mt5.copy_rates_from(stock_name, mt5.TIMEFRAME_M5, datetime(today.year, today.month, today.day),
                                   qtt_candles)
