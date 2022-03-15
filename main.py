from order import BuyOrder, SellOrder
from order_list import OrderList
from order_list_display import OrderListDisplay
from sorting_strategy import HighPriceStrategy


def main():
    new_list = OrderList(HighPriceStrategy())
    OrderListDisplay.display_start()
    new_list.add_order(BuyOrder(20.0, 100))
    new_list.add_order(SellOrder(25.0, 200))
    new_list.add_order(BuyOrder(23.0, 50))
    new_list.add_order(BuyOrder(23.0, 70))
    new_list.remove_order(3)
    new_list.add_order(BuyOrder(28.0, 100))
    print("unsorted list:")
    OrderListDisplay.display_list(new_list)
    print("sorted list:")
    new_list.display_sorted_list()
    print("cheapest sum:")
    new_list.display_cheap()


if __name__ == "__main__":
    main()
