'''
OrderSortingStrategy class, implementation of strategy pattern
HighPriceStrategy sorts list by highest price
'''
from abc import ABC, abstractmethod


class OrderSortingStrategy(ABC):
    @abstractmethod
    def sorted_order_list(self, order_list: list) -> list:
        pass


class HighPriceStrategy(OrderSortingStrategy):
    def sorted_order_list(self, order_list: list) -> list:
        sorted_order_list = []
        for order in sorted(order_list):
            sorted_order_list.append(order)
        return sorted_order_list
