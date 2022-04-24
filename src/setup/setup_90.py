from time import sleep

from src.utils.indicators import Indicators
from src.utils.bars import Bars
from src.setup.notification import Notification

SETUP_NAME = "Larry Williams 9.0"
DEFAULT_N_BARS = 25
SHORT_SMA_VALUE = 9
LONG_SMA_VALUE = 21
MINIMUM_AVG_INCLINATION = 0.2


class Setup90:
    def __init__(self):
        self.__bars = Bars()
        self.__msg = Notification()
        self.indicators = Indicators()
        pass

    def __update_bars(self, stock_name):
        self.__stock_bars = self.__bars.get_stock_bars(stock_name, DEFAULT_N_BARS)
        self.__stock_name = stock_name
        self.__open_prices = self.__stock_bars["open"]
        self.__high_prices = self.__stock_bars["high"]
        self.__low_prices = self.__stock_bars["low"]
        self.__close_prices = self.__stock_bars["close"]

    def __update_indicators(self):
        self.__short_sma: list = self.indicators.simple_moving_average(self.__close_prices, SHORT_SMA_VALUE)
        self.__long_sma: list = self.indicators.simple_moving_average(self.__close_prices, LONG_SMA_VALUE)

    def __check_for_trade(self):
        avg_inclination =((self.__short_sma[-1] * 100) / self.__short_sma[-9] - 100)
        trend = avg_inclination > MINIMUM_AVG_INCLINATION
        if self.__short_sma > self.__long_sma and trend:
            if self.__low_prices[-1] <= self.__short_sma[-1] and self.__close_prices[-1] > self.__short_sma:
                self.__msg.send_notification(SETUP_NAME, self.__stock_name)
        elif self.__short_sma < self.__long_sma and trend:
            if self.__high_prices[-1] >= self.__short_sma[-1] and self.__close_prices[-1] < self.__short_sma:
                self.__msg.send_notification(SETUP_NAME, self.__stock_name)

    def run(self, stock_name: str):
        while True:
            self.__update_bars(stock_name)
            self.__update_indicators()
            self.__check_for_trade()
            sleep(300)
