from Product import Product
#from PhysicalProduct import PhysicalProduct
from Supplier import Supplier
class Inventory:
    def __init__(self):
        self.inventory_list: list[Product]=[]

    def inventory_empty(self) -> bool:
        if self.inventory_list==[]:
            return True
        else:
            return False
    #gets the list of objects for upload to file
    def inventory_list_func(self) -> list:
        inventory_func_list=[]
        for product in self.inventory_list:
            inventory_func_list.append(product.product_information())
        return inventory_func_list

    def add_product(self,product:Product):
        self.inventory_list.append(product)

    def remove_product(self,product_id:str):
        product_item=self.search_product(product_id,1)
        self.inventory_list.remove(product_item)

    def search_product(self,searchID: str,userInput: str):
        for product in self.inventory_list:

            if product.product_information()["ID"]==searchID.getProductID():
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
        
    def display_all(self):
        print("Current Inventory\n"
        "------------------------------------------------")
        #ID: P001 | Name: Laptop | Price: $1200.00 | Stock: 15
        for item in self.inventory_list:
            item.display_information()
        print("------------------------------------------------\n")

'''
sup1=Supplier("1","IBM","ibmemail")
productA=PhysicalProduct("1","Laptop",1999.99,10,1.5,sup1)
inventoryA=Inventory()
inventoryA.add_product(productA)
inventoryA.remove_product(productA)

productA.display_information()
inventoryB=Inventory()
inventoryB.add_product(productA)
productA.display_information()

'''