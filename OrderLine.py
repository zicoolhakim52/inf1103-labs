from Product import Product


class OrderLine:

    def __init__(self, product: Product, quantity: int):
        self.product = product
        if int(quantity)<=0:
            raise ValueError("Quantity must be greater than zero.")
        else:
            self.quantity = int(quantity)

    def calculate_subtotal(self) -> float:
        return self.product.getPrice() * self.quantity

    def display_orderLine(self) -> None:
        self.product.display_ID_Name()
        print(f"quantity: {self.quantity}")

    def output_orderLines(self) -> dict:
        return {
            "productID": self.product.getProductID(),
            "quantity": self.quantity,
        }