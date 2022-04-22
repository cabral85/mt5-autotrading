import trade_system as setups

class Setups():
    def __init__(self):
        return

    
    def run(self, stock_name, price):
        for setup in setups:
            init = setup()
            init.run(stock_name, price)
