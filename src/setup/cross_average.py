from src.setup.notification import Notification
from src.utils.bars import Bars
from src.utils.indicators import simple_moving_average

SETUP_NAME = "Cross Average"
DEFAULT_N_BARS = 100
SHORT_SMA_VALUE = 9
FIVE_MIN_WAIT = 60


class CrossBollingerBands:
    def __init__(self, mt5):
        self.__stock_name = None
        self.mt5 = mt5
        self.__bars = Bars(mt5)
        self.__msg = Notification()

    def __update_bars(self):
        self.__stock_bars = self.__bars.get_stock_bars(self.__stock_name, DEFAULT_N_BARS, self.mt5.TIMEFRAME_M10)
        self.__open_prices = self.__stock_bars["open"]
        self.__high_prices = self.__stock_bars["high"]
        self.__low_prices = self.__stock_bars["low"]
        self.__close_prices = self.__stock_bars["close"]

    def __update_indicators(self):
        self.__short_sma: list = simple_moving_average(self.__close_prices, SHORT_SMA_VALUE)

    def __check_for_trade(self):
        if self.__open_prices[-1] < self.__short_sma[-18] < self.__close_prices[-1]:
            self.__msg.send_notification(f"{SETUP_NAME} - Buy", self.__stock_name)
        elif self.__open_prices[-1] > self.__short_sma[-18] > self.__close_prices[-1]:
            self.__msg.send_notification(f"{SETUP_NAME} - Sell", self.__stock_name)

    def run(self, stock_name):
        self.__stock_name = stock_name
        self.__update_bars()
        self.__update_indicators()
        self.__check_for_trade()
