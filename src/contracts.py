class Contracts(): 
    def getStocks(self):
        lines = []
        with open('stock-list.txt', 'r') as f:
            for line in f:
                lines.append(line.replace('\n', ''))
        return lines

    def getFutureContracts(self):
        lines = []
        with open('future-contracts.txt', 'r') as f:
            for line in f:
                lines.append(line.replace('\n', ''))
        return lines