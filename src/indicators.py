import numpy as np

class Indicators():

    def __init__(self):
        self._price_close_position = 4

    def exponential_moving_average(self, stocks, value):
        # EMA: {Close - EMA(previous day)} x multiplier + EMA(previous day)
        # Multiplier: (2 / (Time periods + 1) ) = (2 / (10 + 1) )
        multiplier = (2/(value+1))
        calculated_prices = []
        last_price = 0
        last_ema = 0
        for price in stocks:
            index = 0
            stock_name = list(price.keys())[0]
            while index < len(price[stock_name]):
                close_price = price[stock_name][index][self._price_close_position]
                ema = close_price - last_price * multiplier + last_ema

                price_list = np.array(price[stock_name][index]).tolist()
                price_values = np.append(price_list, ema)
                calculated_prices.append({stock_name: price_values})

                last_price = close_price
                last_ema = ema
                index += 1
            
    
    def simple_moving_average(self, prices):
        return
