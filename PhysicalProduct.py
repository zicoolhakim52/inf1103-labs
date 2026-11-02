from Product import Product
from CanBeShipped import CanBeShipped
class PhysicalProduct(Product,CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self._weight=weight

    def get_fulfilment_info(self):
        print("Product requires physical shipping")

    def display_information(self):
        super().display_information() 
        print(f"Weight: {self._weight}")

    def calculate_shipping_cost(self):
        #calculate $1 per 1kg
        weight=self._weight * 1
        print(f"Total shipping cost of item is ${round(weight,2)}")

    def product_information(self):
        product_dict=super().product_information()
        product_dict["Weight"]=self._weight
        return product_dict