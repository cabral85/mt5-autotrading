import numpy as np


class Indicators:

    def __init__(self):
        pass

    def simple_moving_average(self, close_prices, average_value):
        index = 0
        calc_prices = []
        average_price = []
        while index < len(close_prices):
            calc_prices.append(close_prices[index])
            if len(calc_prices) >= average_value:
                average_price.append(round(sum(calc_prices[average_value * -1:]) / average_value, 2))
            index += 1

        return average_price

    def top_prices(self, prices):
        high_price = prices["high"]
        tops = []
        last_price = 0
        for high in high_price:
            if high > last_price:
                last_price = high
            elif high < last_price:
                tops.append(last_price)

    def bottom_prices(self, prices):
        low_prices = prices["low"]
        bottoms = []
        last_price = 0
        for low in low_prices:
            if low < last_price:
                last_price = low
            elif low > last_price:
                bottoms.append(last_price)