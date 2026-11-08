from abc import ABC, abstractmethod
from Supplier import Supplier
class Product(ABC):
    def __init__(self,product_id: str,name: str,price: float,stock: int,supplier: Supplier):
        self.__productid = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__supplier=supplier

    @abstractmethod
    def get_fulfilment_info():
        pass

    def display_information(self):
        print(f"ID: {self.__productid} | Name: {self.__name} | Price: {self.__price} | Stock: {self.__stock}", end=" | ")
        self.__supplier.display_information()

    def getStock(self):
        return self.__stock

    def getName(self):
        return self.__name
    #Returns as a dictionary
    def product_information(self):
        return({"ID": self.__productid, "Name": self.__name, "Price": self.__price, "Stock": self.__stock})

    def update_stock(self,new_stock):
        self.__stock= new_stock