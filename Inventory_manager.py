import json

#classes
class Product:
    def __init__(self,product_id,name,price,stock):
        self.__productid = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock


    def display_information(self):
        print(f"ID: {self.__productid} | Name: {self.__name} Price: {self.__price} Stock: {self.__stock}")

    def getStock(self):
        return self.__stock

    def getName(self):
        return self.__name
    #Returns as a dictionary
    def product_information(self):
        return({"ID": self.__productid, "Name": self.__name, "Price": self.__price, "Stock": self.__stock})

    def update_stock(self,new_stock):
        self.__stock= new_stock
        


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

class Main_Program:
    def display_menu():
        print("----------- MENU -----------\n"
        "1. Display All Products\n" 
        "2. Add Product\n" 
        "3. Update Stock\n"
        "4. Search Product\n"
        "5. Save Inventory\n"
        "6. Exit\n"
        "----------------------------\n")
    def get_valid_input():
        #inputStrList=["Enter Product Name: ", "Enter Quantity: "]
        #errorMsgList=["Please enter a valid Product Name or 'quit' to exit: ", "Please enter a valid quantity or 'quit' to exit: "]
        input_Option=""

        while type(input_Option)!=int:
            try:
                input_Option=int(input("Enter option: "))
                if input_Option not in [1,2,3,4,5,6]:
                    print("Invalid option, Please type an option that is displayed")
            except:
                print("Invalid option, Please type an option that is displayed")
                continue
        return(input_Option)
    def get_input_ID(userInput,current_inventory):
        validateInputID=False
        while validateInputID==False:
            search_item= input("Product ID: ")
            validateInput=Main_Program.validateID(search_item)
            #Search if ID already exists
            if validateInput:
                IDExistsCheck=Main_Program.IDExists(search_item,current_inventory,userInput)
                if IDExistsCheck[0]:
                    if userInput==2:
                        print("ID already exists, Please enter another ID")
                    else:
                        validateInputID=True
                        return IDExistsCheck[1]
                else:
                    if userInput==2:
                        return search_item
                    else:
                        print("ID does not exists, Please enter another ID")


    def validateID(productID):
        if productID=="":
            print("Product ID cannot be empty")
            return False
        else:
            first_letter=productID[0]
            if first_letter!="P":
                print("Product ID must start with P (case sensitive)")
                return False
            elif len(productID) != 4:
                print("Product ID must be 4 letters long. e.g. Pxxx where x is an integer")
                return False
            else:
                three_digits=productID[1:3]
                if three_digits.isdigit():
                    return True
                else:
                    print("Please input Pxxx where x is an integer")
                    return False
    def IDExists(ID,current_inventory,userInput):
        search_result=current_inventory.search_product(ID,userInput)
        if search_result[0]:
            return[True,search_result]
        else:
            current_inventory.display_all()
            return[False]

    def validatePrice(productPrice):
        try:
            productPrice=float(productPrice)
            price=round(productPrice,2)
            return [True,price]
        except:
            print("Price must be a int/float")
            return [False]
        
        

class File_Handling:
    ##Opens inventory file. If file does not exist, creates a new inventory file
    def load_inventory(inventoryQuantity):
        try:
            inventoryFile= open("inventory.json",'r+')
            #closes file
            inventoryFile.close()
            print("inventory.json found.")
            
            ##Reads data from file
            with open("inventory.json",'r') as file:
                file_contents = json.load(file)


            #Get amount of stock already in inventory
            for item in file_contents:
                inventoryQuantity+=int(item["Stock"])

            #get inventory number of last items
            lastItem=file_contents[-1]
            #Get the order number of the last item on the list
            lastItemID=lastItem["ID"]
            lastItemID=int(lastItemID[-1])

            print("Inventory loaded successfully.\n")
            return([file_contents,inventoryQuantity,lastItemID])

        except:
            inventoryFile= open("inventory.json",'w+')
            #closes file
            inventoryFile.close()
            
            #empty file
            return("Empty")

    #Adds one order at a time
    def save_inventory(current_inventory,num):
        if num==5:
            print("Saving inventory...")
        else:
            print("Saving inventory before exit...")

        if not current_inventory.inventory_empty():
            with open("inventory.json",'w+') as file:
                json.dump(current_inventory.inventory_list_func(), file,indent=1)

        if num==5:
            print("Inventory saved successfully to inventory.json.")
        else:
            print("Inventory saved successfully.\n")

#Functions

#gets quantity of user input and validates it

#Adds new input to inventory
def process_delivery(current_total, new_value):
    current_total += int(new_value)
    return current_total

#calculates 10% of delivery tax
def calculate_tax(amount):
    amount=int(amount*.10)
    return amount

#Prints out summary
def generate_report(total_units, failed_attempts):
    print("\nYou have exited the inventory management system.")
    print("Total units processed: ", total_units)
    print("Total rejected entries: ", failed_attempts)

#Rejected entries count
def errorCount():
    if not hasattr(errorCount, "count"):
        errorCount.count=0
    errorCount.count +=1
    return errorCount.count



def stockOverflow(inventoryQuantity):
    #if stock is over 500, the program prevents adding more
    if inventoryQuantity>500:
        resultQuantity=False
    else:
        resultQuantity=True
    return(resultQuantity)



##Start of programs
print("======================================== \n"
"INVENTORY MANAGEMENT SYSTEM\n"
"========================================")
#variable holds inventory quantity
inventoryQuantity = 0
#order number of the last item on the list sets to 1001 if no file created before
lastItemNumber=0
current_inventory = Inventory()

##loads inventory (inventory in list)
loaded_inventory=File_Handling.load_inventory(inventoryQuantity)
#current_inventory format= [dictionary of inventory, total number of all stocks, last item ID]
if loaded_inventory != "Empty":
    for item in loaded_inventory[0]:
        product=Product(item["ID"],item["Name"],item["Price"],item["Stock"])
        current_inventory.add_product(product)
    inventoryQuantity=int(loaded_inventory[1])
    lastItemNumber=int(loaded_inventory[2])



#main loop 
while True:
    
    #Prevents adding more than 500 Quantity
    #if inventoryQuantity < 500:
    Main_Program.display_menu()
    userInput= Main_Program.get_valid_input()
    #display inventory
    if userInput==1:
        if current_inventory.inventory_empty():
            print("Inventory is Empty\n")
        else:
            Inventory.display_all(current_inventory)
    #add inventory
    elif userInput==2:
        search_item=Main_Program.get_input_ID(userInput,current_inventory)

        productName=input("Product Name: ")
        validateInputPrice=False
        while validateInputPrice==False:
            productPrice=input("Price: ")
            validateInput=Main_Program.validatePrice(productPrice)
            if validateInput[0]:
                #price is rounded to 2 decimal places
                productPrice=validateInput[1]
                validateInputPrice=True
        validateInputStock=False
        while validateInputStock==False:
            stockQuantity=input("Stock Quantity: ")
            if stockQuantity.isdigit():
                validateInputStock=True
            else:
                print("Stock must be an integer")
        #Create product object
        product=Product(search_item,productName,productPrice,stockQuantity)
        #Add product to inventory object
        current_inventory.add_product(product)

        #current_inventory=Inventory.add_product(current_inventory,inventoryQuantity)
    #update stock
    elif userInput==3:
        print("\nUpdate Stock\n")
        IDExistsCheck=Main_Program.get_input_ID(userInput,current_inventory)

        product_info=IDExistsCheck[1]
        old_stock=product_info.getStock()
        name=product_info.getName()
        print("Name: ", name)
        print("Current Stock: ", old_stock)
        
        new_stock=input("New Stock Quantity: ")

        inventoryQuantity=inventoryQuantity+int(new_stock) - int(old_stock)
        result=stockOverflow(inventoryQuantity)
        if result ==True:
            item["Stock"]=new_stock
            product_info.update_stock(new_stock)
            
            print("\nStock updated successfully!\n")
        else:
            inventoryQuantity=inventoryQuantity- int(new_stock) + int(old_stock)
            print("Quantity would go over 500. Item not added")
                
    #Search Product
    elif userInput==4:
        search_result=Main_Program.get_input_ID(userInput,current_inventory)
        product=search_result[1]
        product.display_information()
    elif userInput==5:
        File_Handling.save_inventory(current_inventory,"Manual Save")
    elif userInput==6:
        File_Handling.save_inventory(current_inventory,"Auto Save")
        print("Thank you for using Inventory Management System.\n"
        "Program terminated.")
        break


           

