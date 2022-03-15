'''
class OrderList, also not abstract for simplicity,
3 attributes:
strategy object used in sorting (implementation of strategy pattern) passed in init
getters, iterator implemented
get_sorted_list returns sorted list using strategy object
display_sorted_list prints all elements on screen using OrderListDisplay class
generate_new_id returns int, generates id for new element in list, self-incrementing by 1 each time
add/remove order: adds or removes order to the list, also prints message on screen
display_cheap: displays cost (price*qty) of cheapest (per item) order in list
'''
from order import Order
from order_list_display import OrderListDisplay
from sorting_strategy import OrderSortingStrategy


class OrderList:
    def __init__(self, strategy: OrderSortingStrategy):
        self._strategy = strategy
        self._list = []
        self._items = 0

    def get_list(self) -> list:
        return self._list

    def get_sorted_list(self) -> list:
        return self._strategy.sorted_order_list(self._list)

    def display_sorted_list(self):
        OrderListDisplay.display_list(self.get_sorted_list())

    def generate_new_id(self):
        self._items += 1
        return self._items

    def add_order(self, order: Order):
        order.set_id(self.generate_new_id())
        OrderListDisplay.display_add(order)
        self._list.append(order)

    def remove_order(self, i_d: int):
        OrderListDisplay.display_remove(self._list[i_d])
        del self._list[i_d]

    def display_cheap(self):
        sorted_list = self.get_sorted_list()
        OrderListDisplay.display_cheapest_sum(sorted_list[0])

    def __iter__(self):
        return OrderListIterator(self)


class OrderListIterator:
    def __init__(self, order_list: OrderList):
        self._order_list = order_list
        self._index = 0

    def __next__(self):
        if self._index < len(self._order_list.get_list()):
            result = self._order_list.get_list()[self._index]
            self._index += 1
            return result
        raise StopIteration
