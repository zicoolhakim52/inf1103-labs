from abc import ABC, abstractmethod
from Supplier import Supplier


class Product(ABC):

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        supplier: Supplier,
    ):
        self.__productid = product_id
        self.__name = name
        if float(price)<=0:
            raise ValueError("Price must be greater than zero.")
        else:
            self.__price = price
        if int(stock)<=0:
            raise ValueError("Stock must be greater than zero.")
        else:
            self.__stock = stock
        self.__supplier = supplier

    @abstractmethod
    def get_fulfilment_info() -> str:
        pass

    @abstractmethod
    def get_product_type():
        pass

    def display_information(self) -> None:
        print(
            f"ID: {self.__productid} | Name: {self.__name} | Price: {self.__price} | Stock: {self.__stock}",
            end=" | ",
        )
        self.__supplier.display_information()

    def display_ID_Name(self) -> None:
        print(f"ID: {self.__productid} | Name: {self.__name}", end=" | ")

    def getStock(self) -> int:
        return self.__stock

    def getName(self) -> str:
        return self.__name

    def getProductID(self) -> str:
        return self.__productid

    def getPrice(self) -> float:
        return self.__price

    def product_information(self) -> dict:
        return {
            "ID": self.__productid,
            "Name": self.__name,
            "Price": self.__price,
            "Stock": self.__stock,
            "SupplierID": self.__supplier._supplier_id,
            "SupplierName": self.__supplier._name,
            "SupplierEmail": self.__supplier._contact_email,
        }

    def update_stock(self, new_stock: int) -> None:
        self.__stock = new_stock

    def get_positive_float(prompt: str) -> float:
        while True:
            try:
                value = float(input(prompt))
                if value <= 0:
                    print("Please enter a number greater than zero.")
                continue
                return value
            except ValueError:
                print("Please enter a valid number, e.g. 12.50")

