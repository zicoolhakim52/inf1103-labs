from Product import Product
from Supplier import Supplier


class DigitalProduct(Product):

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        download_size: float,
        supplier: Supplier,
    ):
        super().__init__(product_id, name, price, stock, supplier)
        self._download_size = download_size

    def get_fulfilment_info(self) -> str:
        return "Product is delivered digitally"

    def get_product_type(self) -> str:
        return "digital"

    def display_information(self) -> None:
        super().display_information()
        print(f"Download size: {self._download_size}")

    def product_information(self) -> dict:
        product_dict = super().product_information()
        product_dict["uniqueTrait"] = self._download_size
        return product_dict