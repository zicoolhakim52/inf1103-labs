from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier
class Inventory:
    def __init__(self):
        self.products: list[Product]=[]

    def inventory_empty(self) -> bool:
        if self.products==[]:
            return True
        else:
            return False
    #gets the list of objects for upload to file
    def inventory_list_func(self) -> list:
        inventory_func_list=[]
        for product in self.products:
            inventory_func_list.append(product.product_information())
        return inventory_func_list

    def add_product(self,product:Product)-> None:
        self.products.append(product)

    def remove_product(self,product:Product) -> None:
        product_item=self.find_product(product,1)
        self.products.remove(product_item)

    def find_product(self,productID: str,userInput: str) -> Product | None:
        for product in self.products:
            if product.product_information()["ID"]==productID:
                if userInput!=2:
                    print("\nProduct Found!\n")
                else:
                    print("ID is taken")
                
                return product
        if userInput!=2:
            print("No product Found")
        else:
            print("ID not taken")
        
        return None
        
    def display_all(self)-> None:
        print("Current Inventory\n"
        "------------------------------------------------")
        #ID: P001 | Name: Laptop | Price: $1200.00 | Stock: 15
        for item in self.products:
            item.display_information()
        print("------------------------------------------------\n")

    



'''
def display_all_products(self) -> None:
        for product in self.products:
            product.display_information()
            
def show_product_details(product: Product) -> None:
        product.display_information()
        print(product.get_fulfilment_info())

sup1=Supplier("1","IBM","ibmemail")
productA=PhysicalProduct("1","Laptop",1999.99,10,1.5,sup1)
productB=DigitalProduct("2","COD WAW",12,100,20,sup1)
inventoryA=Inventory()
inventoryA.add_product(productA)
inventoryA.add_product(productB)
inventoryA.display_all_products()
show_product_details(productA)
show_product_details(productB)

'''