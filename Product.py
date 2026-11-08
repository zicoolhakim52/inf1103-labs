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
    def get_fulfilment_info()-> str:
        pass

    def display_information(self)-> None:
        print(f"ID: {self.__productid} | Name: {self.__name} | Price: {self.__price} | Stock: {self.__stock}", end=" | ")
        self.__supplier.display_information()

    def getStock(self)-> int:
        return self.__stock

    def getName(self)-> str:
        return self.__name
    
    def getProductID(self)-> str:
        return self.__productid

    def getPrice(self)-> float:
        return self.__price
    #Returns as a dictionary
    def product_information(self)-> dict:
        return({"ID": self.__productid, "Name": self.__name, "Price": self.__price, "Stock": self.__stock, "SupplierID": self.__supplier._supplier_id,"SupplierName": self.__supplier._name, "SupplierEmail": self.__supplier._contact_email})

    def update_stock(self,new_stock)-> None:
        self.__stock= new_stock

