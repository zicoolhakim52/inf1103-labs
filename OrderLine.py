from Product import Product
class OrderLine:
    def __init__(self,product: Product,quantity: float):
        self.product=product
        self.quantity=quantity

    def calculate_subtotal(self) -> float:
        return self.product.getPrice() * self.quantity

    def display_orderLine(self)-> None:
        self.product.display_information()