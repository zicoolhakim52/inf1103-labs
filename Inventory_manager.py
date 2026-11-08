from DigitalProduct import DigitalProduct
from PhysicalProduct import PhysicalProduct
from Inventory import Inventory
from File_Handling import File_Handling
from Main_Program import Main_Program
from Supplier import Supplier
   
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
'''
#Prints out summary
def generate_report(total_units, failed_attempts):
    print("\nYou have exited the inventory management system.")
    print("Total units processed: ", total_units)
    print("Total rejected entries: ", failed_attempts)'''

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


def get_product_class(search_item,productName,productPrice,stockQuantity,product_type,supplierinfo):
    if product_type=="Digital":
        download_size_input=Main_Program.get_valid_digital_input()
        product=DigitalProduct(search_item,productName,productPrice,stockQuantity,download_size_input,supplierinfo)
    else:
        product_weight_input=Main_Program.get_valid_weight_input()
        product=PhysicalProduct(search_item,productName,productPrice,stockQuantity,product_weight_input,supplierinfo)
    return product


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
        supplier_info=Supplier(item["SupplierID"],item["SupplierName"],item["SupplierEmail"])
        if "Download size" in item.keys():
            product=DigitalProduct(item["ID"],item["Name"],item["Price"],item["Stock"],item["Download size"],supplier_info)
        else:
            product=PhysicalProduct(item["ID"],item["Name"],item["Price"],item["Stock"],item["Weight"],supplier_info)
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
        product_type=Main_Program.get_product_type()
        search_item=Main_Program.get_input_ID(userInput,current_inventory)
        productName=input("Product Name: ")
        productPrice=Main_Program.get_product_price()
        stockQuantity=Main_Program.get_valid_stock()
        supplierID=input("Enter Supplier ID: ")
        supplierName=input("Enter Supplier Name: ")
        supplierEmail=input("Enter Supplier Email: ")
        supplierinfo=Supplier(supplierID,supplierName,supplierEmail)
        product=get_product_class(search_item,productName,productPrice,stockQuantity,product_type,supplierinfo)
                    
        #Create product object
        #Add product to inventory object
        current_inventory.add_product(product)

        #current_inventory=Inventory.add_product(current_inventory,inventoryQuantity)
    #update stock
    elif userInput==3:
        print("\nUpdate Stock\n")
        IDExistsCheck=Main_Program.get_input_ID(userInput,current_inventory)

        product_info=IDExistsCheck
        old_stock=product_info.getStock()
        name=product_info.getName()
        print("Name: ", name)
        print("Current Stock: ", old_stock)
        
        new_stock=input("New Stock Quantity: ")
        #Update total inventory
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
        product=search_result
        product.display_information()
    elif userInput==5:
        File_Handling.save_inventory(current_inventory,"Manual Save")
    elif userInput==6:
        File_Handling.save_inventory(current_inventory,"Auto Save")
        print("Thank you for using Inventory Management System.\n"
        "Program terminated.")
        break


           

