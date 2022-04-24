import numpy as np

class Indicators():

    def __init__(self):
        pass

    def exponential_moving_average(self, stock, value):
        # EMA: {Close - EMA(previous day)} x multiplier + EMA(previous day)
        # Multiplier: (2 / (Time periods + 1) ) = (2 / (10 + 1) )
        multiplier = (2/(value+1))
        calculated_prices = []
        last_price = 0
        last_ema = 0

        index = 0
        stock_name = list(stock.keys())[0]
        while index < len(stock[stock_name]):
            close_price = stock[stock_name][index][self._price_close_position]
            ema = close_price - last_price * multiplier + last_ema

            price_list = np.array(stock[stock_name][index]).tolist()
            price_values = np.append(price_list, ema)
            calculated_prices.append({stock_name: price_values})

            last_price = close_price
            last_ema = ema
            index += 1
            
    
    def simple_moving_average(self, close_prices, average_value):
        index = 0
        calc_prices = []
        average_price = []
        while index < len(close_prices):
            calc_prices.append(close_prices)
            if len(calc_prices) >= average_value:
                average_price.append(round(sum(calc_prices[average_value*-1:]) / average_value, 2))
            index += 1

        return average_price
