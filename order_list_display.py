'''
OrderListDisplay, contains class methods used for display purpose
'''
from order import Order, BuyOrder


class OrderListDisplay:
    first_line = "Id  Order Type    Price Quantity"

    @classmethod
    def construct_line(cls, order: Order, order_type: str) -> list:
        line = [f"{order.get_id():03d}"]
        if isinstance(order, BuyOrder):
            line.append("Buy  ")
        else:
            line.append("Sell ")
        line.append(order_type)
        line.append(f"{order.get_price():5}")
        line.append(f"{order.get_quantity():8}")
        return line

    @classmethod
    def display_start(cls):
        print(cls.first_line)

    @classmethod
    def display_list(cls, order_list):
        for order in order_list:
            line = cls.construct_line(order, "display")
            print(" ".join(line))

    @classmethod
    def display_add(cls, order):
        line = cls.construct_line(order, "add    ")
        print(" ".join(line))

    @classmethod
    def display_remove(cls, order):
        line = cls.construct_line(order, "remove ")
        print(" ".join(line))

    @classmethod
    def display_cheapest_sum(cls, order):
        line = [f"{order.get_id():03d}"]
        if isinstance(order, BuyOrder):
            line.append("Buy  ")
        else:
            line.append("Sell ")
        line.append("cheap")
        line.append(f"{order.get_price()*order.get_quantity():16}")
        print(" ".join(line))
