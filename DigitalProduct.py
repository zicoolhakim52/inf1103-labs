from Product import Product
from Supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self._download_size=download_size

    def get_fulfilment_info(self)-> str:
        return ("Product is delivered digitally")

    def display_information(self)-> None:
        super().display_information() 
        print(f"Download size: {self._download_size}")

    def product_information(self) -> dict:
        product_dict=super().product_information()
        product_dict["Download size"]=self._download_size
        return product_dict
    



'''
sup1=Supplier("1","IBM","ibmemail")
dproduct=DigitalProduct("1","CallOfDuty",100.99,10,190.5,sup1)
del sup1
dproduct.display_information()
#output
#ID: 1 | Name: CallOfDuty | Price: 100.99 | Stock: 10 | Supplier name: IBM | Supplier ID: 1 | Supplier Email:ibmemail | Download size: 190.5
'''