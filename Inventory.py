from DigitalProduct import DigitalProduct
from PhysicalProduct import PhysicalProduct
from Product import Product
from Supplier import Supplier


class Inventory:

    def __init__(self):
        self.products: list[Product] = []

    def inventory_empty(self) -> bool:
        if self.products == []:
            return True
        else:
            return False

    def getproducts(self) -> list[Product]:
        return self.products

    def inventory_list_func(self) -> list:
        inventory_func_list = []
        for product in self.products:
            product_dict=product.product_information()
            product_dict["Type"]= product.get_product_type()
            inventory_func_list.append(product_dict)
        return inventory_func_list

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        product_item = self.find_product(product)
        self.products.remove(product_item)

    def find_product(self, productInput: Product) -> Product | None:
        for product in self.products:
            if product.product_information()["ID"] == productInput.getProductID():
                return product
        return None

    def search_product_by_ID(self, searchID, userInput) -> Product | None:
        for product in self.products:
            if product.product_information()["ID"] == searchID:
                if userInput != 2:
                    print("\nProduct Found!\n")
                else:
                    print("ID is taken")
                return product
        if userInput != 2:
            print("No product Found")
        else:
            print("ID not taken")
        return None

    def display_all(self) -> None:
        print(
            "Current Inventory\n"
            "------------------------------------------------"
        )
        for item in self.products:
            item.display_information()
        print("------------------------------------------------\n")