class Inventory:
    def __init__(self):
        self.__inventorylist=[]

    def add_product(self,product):
        self.__inventorylist.append(product)

    def printproduct(self):
        for i in self.__inventorylist:
            i.displayProduct()

class Product:
    def __init__(self,id,name,price,stock):
        self.__ID=id
        self.__name=name
        self.__price=price
        self.__stock=stock
        
    def displayProduct(self):
        print(self.__ID)
        print(self.__name)
        print(self.__price)
        print(self.__stock)





inventory = Inventory() # creating the inventory object from the Inventory class
product1 = Product("P001", "Laptop", 1200.00, 15) # creating product from Product class, via init
product2 = Product("P002", "Mouse", 25.50, 40)
product2.displayProduct()
inventory.add_product(product1) # pass the product to inventory class to store in a list
inventory.add_product(product2)
inventory.printproduct()