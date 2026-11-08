from OrderLine import OrderLine
from Product import Product
from Supplier import Supplier
from PhysicalProduct import PhysicalProduct
class Order:
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self)-> float:
        total=0
        for product in self.order_lines:
            total+=product.calculate_subtotal()
        return total

    def display_order(self):
        for product in self.order_lines:
            product.display_orderLine()

'''
order1=Order("1")

sup1=Supplier("1","IBM","ibmemail")
productA=PhysicalProduct("1","Laptop",2000,10,1.5,sup1)
productB=PhysicalProduct("2","Laptop case",20,10,0.1,sup1)
order1.add_order_line(productA,10)
order1.add_order_line(productB,10)

print(order1.display_order())
print(order1.calculate_total())

order2=Order("2")
order2.add_order_line(productA,10)

'''
