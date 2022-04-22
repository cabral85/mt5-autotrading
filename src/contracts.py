class Contracts(): 
    def get_stocks(self):
        lines = []
        with open('resource/stock-list.txt', 'r') as f:
            for line in f:
                lines.append(line.replace('\n', ''))
        return lines

    def get_future_contracts(self):
        lines = []
        with open('resource/future-contracts.txt', 'r') as f:
            for line in f:
                lines.append(line.replace('\n', ''))
        return lines