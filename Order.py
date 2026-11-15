from BulkDiscount import BulkDiscount
from DiscountStrategy import DiscountStrategy
from NoDiscount import NoDiscount
from OrderLine import OrderLine
from PercentageDiscount import PercentageDiscount
from PhysicalProduct import PhysicalProduct
from Product import Product
from Supplier import Supplier


class Order:

    def __init__(
        self, order_id: str, discount: DiscountStrategy = NoDiscount
    ) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        self.order_discount: float = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = sum(line.calculate_subtotal() for line in self.order_lines)
        return self.discount.apply(total)

    def display_order(self) -> None:
        for product in self.order_lines:
            product.display_orderLine()

    def set_discount(self, new_discount) -> None:
        self.order_discount = new_discount

    def get_id(self) -> str:
        return self.order_id

    def get_order_lines(self) -> list[OrderLine]:
        return self.order_lines