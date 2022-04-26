import MetaTrader5 as mt5
# exibimos dados sobre o pacote MetaTrader5
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
 
# estabelecemos a conexão ao MetaTrader 5
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 
# obtemos todos os símbolos
symbols=mt5.symbols_get()
print('Symbols: ', len(symbols))
count=0
# exibimos os 5 primeiros
stocks = []
for symbol in symbols:
    if len(symbol.name) == 5:
        stocks.append(symbol.name)

stocks.sort()

with open('list.txt', 'w') as f:
    for stock in stocks:
        f.write(f"{stock}\n")