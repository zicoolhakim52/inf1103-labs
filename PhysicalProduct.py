from Product import Product
from Supplier import Supplier
from CanBeShipped import CanBeShipped
class PhysicalProduct(Product,CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock,supplier)
        self._weight=weight

    def get_fulfilment_info(self)-> None:
        print("Product requires physical shipping")

    def display_information(self)-> None:
        super().display_information() 
        print(f"Weight: {self._weight}")

    def calculate_shipping_cost(self)-> None:
        #calculate $1 per 1kg
        weight=self._weight * 1
        print(f"Total shipping cost of item is ${round(weight,2)}")

    def product_information(self) -> dict:
        product_dict=super().product_information()
        product_dict["Weight"]=self._weight
        return product_dict

'''
sup1=Supplier("1","IBM","ibmemail")
pproduct=PhysicalProduct("1","Hakim",122.00,12,10.0,sup1)
del sup1
pproduct.display_information()
#output
#ID: 1 | Name: Hakim | Price: 122.0 | Stock: 12 | Supplier name: IBM | Supplier ID: 1 | Supplier Email:ibmemail | Weight: 10.0

'''