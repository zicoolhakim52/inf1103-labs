from CanBeShipped import CanBeShipped
from Product import Product
from Supplier import Supplier


class PhysicalProduct(Product, CanBeShipped):

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        weight: float,
        supplier: Supplier,
    ):
        super().__init__(product_id, name, price, stock, supplier)
        self._weight = weight

    def get_fulfilment_info(self) -> str:
        return "Product requires physical shipping"

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self._weight}")

    def calculate_shipping_cost(self) -> None:
        weight = self._weight * 1
        return weight

    def product_information(self) -> dict:
        product_dict = super().product_information()
        product_dict["Weight"] = self._weight
        return product_dict