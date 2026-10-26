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

    def update_stock(self):
        self.__stock= new_stock
        


class Inventory:
    def __init__(self):
        self.__inventory_list=[]

    def add_product(self,product):
        self.__inventory_list.append(product)
        '''
        #temp dictionary to add new items
        add_product_dictionary={}
        print("Add New Product\n")
        #input statments
        add_product_dictionary["ID"]= input("Product ID: ")
        add_product_dictionary["Name"]=input("Product Name: ")
        add_product_dictionary["Price"]=input("Price: ")
        new_stock=input("Stock Quantity: ")
        add_product_dictionary["Stock"]=new_stock
        inventoryQuantity+=int(new_stock)

        result=stockOverflow(inventoryQuantity)
        if result==True:
            #Add to the current inventory list
            current_inventory.append(add_product_dictionary)
            print("\nProduct added successfully!\n")
        else:
            inventoryQuantity-=int(new_stock)
            print("Quantity would go over 500. Item not added\n")
        return(current_inventory)'''


    def search_product(self,searchID):
        for product in self.__inventory_list:
            if product.__productid==searchID:
                product.Product.display_information()
                return
        print("Product not found")
        

        '''
        #current_inventory,ID_lookup,"print Item"/"update Item"
        current_inventory, ID_lookup, actionRequired=searchQureies
        result="Product not found.\n"
        ID_exists=False
        for item in current_inventory:
            itemID=item["ID"]
            selectedItem=item
            if itemID==ID_lookup:
                result="Product Found:\n"
                ID_exists=True
                break
        if(actionRequired=="print Item"):
            print("Product Found")
            print("------------------------------------------------")
            print("ID: ", selectedItem["ID"])
            print("Name: ", selectedItem["Name"])
            print("Price: ", selectedItem["Price"])
            print("Stock: ", selectedItem["Stock"])
            print("------------------------------------------------\n")
        else:
            print(result)

        return(ID_exists)'''

        
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
        inputList=[]
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

        if current_inventory!= "Empty":
            with open("inventory.json",'w+') as file:
                json.dump(current_inventory, file,indent=1)

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
    current_inventory=loaded_inventory[0]
    inventoryQuantity=int(loaded_inventory[1])
    lastItemNumber=int(loaded_inventory[2])



#main loop 
while True:
    
    #Prevents adding more than 500 Quantity
    #if inventoryQuantity < 500:
    Main_Program.display_menu()
    userInput= Main_Program.get_valid_input()
    if userInput==1:
        if current_inventory== []:
            print("Inventory is Empty\n")
        else:
            Inventory.display_all(current_inventory)
    elif userInput==2:
        productID= input("Product ID: ")
        productName=input("Product Name: ")
        productPrice=input("Price: ")
        stockQuantity=input("Stock Quantity: ")
        #Create product object
        product=Product(productID,productName,productPrice,stockQuantity)
        #Add product to inventory object
        inventory.add_product(product)

        #current_inventory=Inventory.add_product(current_inventory,inventoryQuantity)
    elif userInput==3:
        print("\nUpdate Stock\n")
        ID_lookup=input("Enter Product ID:")
        search_result=Inventory.search_product(current_inventory,ID_lookup,"update Item")
        if search_result==True:
            for item in current_inventory:
                itemID=item["ID"]
                if itemID==ID_lookup:
                    print("Name: ", item["Name"])
                    print("Current Stock: ", item["Stock"])
                    old_stock=item["Stock"]
                    new_stock=input("New Stock Quantity: ")

                    inventoryQuantity=inventoryQuantity+int(new_stock) - int(old_stock)
                    result=stockOverflow(inventoryQuantity)
                    if result ==True:
                        item["Stock"]=new_stock
                        
                        print("\nStock updated successfully!\n")
                    else:
                        inventoryQuantity=inventoryQuantity- int(new_stock) + int(old_stock)
                        print("Quantity would go over 500. Item not added")
                    break
                
            current_inventory=Product.update_stock(new_stock)
    elif userInput==4:
        search_item=input("Enter Product ID: ")
        search_result=Inventory.search_product(current_inventory,search_item,"print Item")
    elif userInput==5:
        File_Handling.save_inventory(current_inventory,"Manual Save")
    elif userInput==6:
        File_Handling.save_inventory(current_inventory,"Auto Save")
        print("Thank you for using Inventory Management System.\n"
        "Program terminated.")
        break


           

