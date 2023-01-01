import random
from typing import Optional

import MetaTrader5


class Order:
    def __init__(self, mt5: MetaTrader5):
        self.pending_orders = []
        self.mt5 = mt5
        pass

    def add_buy_position(self, symbol, lot, price, take_profit, stop_loss):
        point = self.mt5.symbol_info(symbol).point
        deviation = 20
        request = {
            "action": self.mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": self.mt5.ORDER_TYPE_BUY_LIMIT,
            "price": price,
            "sl": price - stop_loss * point,
            "tp": price + take_profit * point,
            "deviation": deviation,
            "magic": random.randint,
            "type_time": self.mt5.ORDER_TIME_GTC,
            "type_filling": self.mt5.ORDER_FILLING_RETURN,
        }

        result = self.mt5.order_send(request)
        self.log_position_status(result)

    def add_sell_position(self, symbol, lot, price, take_profit, stop_loss):
        point = self.mt5.symbol_info(symbol).point
        deviation = 20
        request = {
            "action": self.mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": self.mt5.ORDER_TYPE_SELL_LIMIT,
            "price": price,
            "sl": price - stop_loss * point,
            "tp": price + take_profit * point,
            "deviation": deviation,
            "magic": random.randint,
            "type_time": self.mt5.ORDER_TIME_GTC,
            "type_filling": self.mt5.ORDER_FILLING_RETURN,
        }

        result = self.mt5.order_send(request)
        self.log_position_status(result)

    def log_position_status(self, result, is_cancel: Optional[bool] = False):
        if result.retcode != self.mt5.TRADE_RETCODE_DONE and ~is_cancel:
            print("2. order_send failed, ret code={}".format(result.retcode))
            # request the result as a dictionary and display it element by element
            result_dict = dict(result)
            for field in result_dict.keys():
                print("   {}={}".format(field, result_dict[field]))
                # if this is a trading request structure, display it element by element as well
                if field == "request":
                    trade_request_dict = dict(result_dict[field])
                    for trader_filed in trade_request_dict:
                        print("       trade request: {}={}".format(trader_filed, trade_request_dict[trader_filed]))
        else:
            self.pending_orders.append(result.order)

    def verify_and_remove_pending_orders(self):
        if len(self.pending_orders) > 0:
            for pending_order in self.pending_orders:
                if self.mt5.position_get(ticket=pending_order):
                    request = {
                        "action": self.mt5.TRADE_ACTION_REMOVE,
                        "order": pending_order
                    }
                    result = self.mt5.order_send(request)
                    self.log_position_status(result, True)
