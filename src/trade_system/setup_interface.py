from abc import ABC, abstractmethod


class SetupInterface(ABC):

    @abstractmethod
    def __get_indicators(self, prices):
        pass

    @abstractmethod
    def run(self, stock_name, prices):
        pass
