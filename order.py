'''
class Order, did not make it abstract for simplicity, in bigger project I would.
3 attributes:
float price and int quantity, both passed in init
int id: initialized as 0, modified when added to list
getters, setters and dunders (used for sorting)
2 subclasses, the only point for them is to make display easier by checking instance Buy/Sell
'''


class Order:

    def __init__(self, price: float, quantity: int):
        self._price = price
        self._quantity = quantity
        self._id = 0

    def get_price(self) -> float:
        return self._price

    def get_quantity(self) -> int:
        return self._quantity

    def get_id(self) -> int:
        return self._id

    def set_id(self, i_d: int):
        self._id = i_d

    def __lt__(self, other):
        return True if self.get_price() < other.get_price() else False

    def __le__(self, other):
        return True if self.get_price() <= other.get_price() else False

    def __eq__(self, other):
        return True if self.get_price() == other.get_price() else False

    def __gt__(self, other):
        return True if self.get_price() > other.get_price() else False

    def __ge__(self, other):
        return True if self.get_price() <= other.get_price() else False


class BuyOrder(Order):
    def __init__(self, price: float, quantity: int):
        super().__init__(price, quantity)


class SellOrder(Order):
    def __init__(self, price: float, quantity: int):
        super().__init__(price, quantity)
