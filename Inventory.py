class Inventory:
    def __init__(self):
        self.__inventory_list=[]

    def inventory_empty(self):
        if self.__inventory_list==[]:
            return True
        else:
            return False
    #gets the list of objects for upload to file
    def inventory_list_func(self):
        inventory_func_list=[]
        for product in self.__inventory_list:
            inventory_func_list.append(product.product_information())
        return inventory_func_list

    def add_product(self,product):
        self.__inventory_list.append(product)

    def search_product(self,searchID,userInput):
        for product in self.__inventory_list:
            
            if product.product_information()["ID"]==searchID:
                if userInput!=2:
                    print("\nProduct Found!\n")
                    return [True,product]
                else:
                    print("ID is taken")
                    return [True]
        if userInput!=2:
            print("No product Found")
            return [False]
        else:
            print("ID not taken")
            return [False]
        
    def display_all(self):
        print("Current Inventory\n"
        "------------------------------------------------")
        #ID: P001 | Name: Laptop | Price: $1200.00 | Stock: 15
        for item in self.__inventory_list:
            item.display_information()
        print("------------------------------------------------\n")