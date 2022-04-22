from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import MetaTrader5 as mt5

from src.contracts import Contracts

class AutoTrading:
    def __init__(self):
        self.__create_connection()
        self.default_candles_qtt = 50

        contracts = Contracts()
        stocks = contracts.getStocks()
        futures = contracts.getFutureContracts()

        self._futures_prices = self.__initialize_stock_price(futures)
        self._stock_prices = self.__initialize_stock_price(stocks)
        


    def __create_connection(self):
        if not mt5.initialize():
            print("mt5 initialize() failed")
            mt5.shutdown()
            
        print(mt5.terminal_info())
        print(mt5.version())

    def __get_stock_price(self, stock, qttCandles):
        return mt5.copy_rates_from(stock, mt5.TIMEFRAME_M5, datetime(2022, 4, 22), qttCandles)

    def __initialize_stock_price(self, stocks):
        stock_prices = []
        for stock in stocks:
            price = self.__get_stock_price(stock, self.default_candles_qtt)
            stock_prices.append({stock: price})
        return stock_prices

    def __checkSetups(self):
        return

run = AutoTrading()
