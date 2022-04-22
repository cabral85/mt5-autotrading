from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import MetaTrader5 as mt5

class AutoTrading:
    def __init__(self):
        self.__createConnection()
        self.__getStocks()

    def __createConnection(self):
        if not mt5.initialize():
            print("initialize() failed")
            mt5.shutdown()
            
        print(mt5.terminal_info())
        print(mt5.version())

    def __getStocks(self):
        wdo_rates =  mt5.copy_rates_from("WDOK22", mt5.TIMEFRAME_M5, datetime(2022,4,22), 1000)
        for val in wdo_rates: 
            print(val)

    def __checkSetups(self):
        return

run = AutoTrading()
