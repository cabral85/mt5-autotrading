import numpy as np

class Indicators():

    def __init__(self):
        self._price_close_position = 4

    def exponential_moving_average(self, stocks, value: int):
        # EMA = Closing price x multiplier + EMA (previous day) x (1-multiplier)
        calculated_prices = []
        last_price = 0
        for stock in stocks:
            index = 0
            stock_name = list(stock.keys())[0]
            while index < len(stock[stock_name]):
                close_price = stock[stock_name][index][self._price_close_position]
                ema = close_price * value + last_price * 1-value

                price_list = np.array(stock[stock_name][index]).tolist()

                price_values = np.append(price_list, ema)
                calculated_prices.append({stock_name: price_values})
                index += 1
            
    
    def simple_moving_average(self, prices):
        return
