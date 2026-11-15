from DigitalProduct import DigitalProduct
from File_Handling import File_Handling
from Inventory import Inventory
from Main_Program import Main_Program
from Order import Order
from PhysicalProduct import PhysicalProduct
from Supplier import Supplier
from ProductFactory import ProductFactory


def process_delivery(current_total, new_value):
    current_total += int(new_value)
    return current_total


def calculate_tax(amount):
    amount = int(amount * 0.10)
    return amount


def errorCount():
    if not hasattr(errorCount, "count"):
        errorCount.count = 0
    errorCount.count += 1
    return errorCount.count


def stockOverflow(inventoryQuantity):
    if inventoryQuantity > 500:
        resultQuantity = False
    else:
        resultQuantity = True
    return resultQuantity


def get_product_class(
    search_item,
    productName,
    productPrice,
    stockQuantity,
    product_type,
    supplierinfo,
):
    if product_type.lower() == "digital":
        unique_trait = Main_Program.get_valid_digital_input()
    else:
        unique_trait = Main_Program.get_valid_weight_input()
        
    product=ProductFactory.create(product_type.lower(),search_item,productName,productPrice,stockQuantity,supplierinfo,unique_trait)
    return product



print(
    "======================================== \n"
    "INVENTORY MANAGEMENT SYSTEM\n"
    "========================================"
)

#Creating an inventory class
current_inventory = Inventory()

#Loading Inventory, supplier and order files
current_inventory = File_Handling.load_inventory(current_inventory)
supplier_list = File_Handling.load_supplier()
orderlist = File_Handling.load_order(current_inventory)

while True:
    Main_Program.display_menu()
    userInput = Main_Program.get_valid_input()

    if userInput == 1:
        if current_inventory.inventory_empty():
            print("Inventory is Empty\n")
        else:
            Inventory.display_all(current_inventory)

    elif userInput == 2:
        product_type = Main_Program.get_product_type()
        search_item = Main_Program.get_input_ID(userInput, current_inventory)
        productName = input("Product Name: ")
        productPrice = Main_Program.get_product_price()
        stockQuantity = Main_Program.get_valid_stock()
        #display suppliers
        Main_Program.get_supplier_list(supplier_list)
        supplierinfo = Main_Program.input_supplier_id(Main_Program.get_supplier_id_list(supplier_list),supplier_list)
        
        '''supplierName = input("Enter Supplier Name: ")
        supplierEmail = input("Enter Supplier Email: ")
        supplierinfo = Supplier(supplierID, supplierName, supplierEmail)'''
        product = get_product_class(
            search_item,
            productName,
            productPrice,
            stockQuantity,
            product_type,
            supplierinfo,
        )
        current_inventory.add_product(product)

    elif userInput == 3:
        print("\nUpdate Stock\n")
        IDExistsCheck = Main_Program.get_input_ID(userInput, current_inventory)

        product_info = IDExistsCheck
        old_stock = product_info.getStock()
        name = product_info.getName()
        print("Name: ", name)
        print("Current Stock: ", old_stock)

        new_stock = input("New Stock Quantity: ")
        
        product_info.update_stock(new_stock)
        print("\nStock updated successfully!\n")

    elif userInput == 4:
        search_result = Main_Program.get_input_ID(userInput, current_inventory)
        product = search_result
        product.display_information()

    elif userInput == 5:
        File_Handling.save_inventory(current_inventory, "Manual Save")

    elif userInput == 6:
        File_Handling.save_inventory(current_inventory, "Auto Save")
        print("Thank you for using Inventory Management System.\nProgram terminated.")
        break

    elif userInput == 7:
        inside_supplier_loop = True
        while inside_supplier_loop == True:
            print(
                "----------- Suppliers -----------\n"
                "1. View Suppliers\n"
                "2. Add Supplier\n"
                "3. Save and Exit\n"
                "----------------------------\n"
            )
            userInputSupplier = Main_Program.get_valid_supplier_input()
            if userInputSupplier == 1:
                Main_Program.get_supplier_list(supplier_list)
            elif userInputSupplier == 2:
                supplierID = input("Enter Supplier ID: ")
                supplierName = input("Enter Supplier Name: ")
                supplierEmail = input("Enter Supplier Email: ")
                supplierinfo = Supplier(supplierID, supplierName, supplierEmail)
                supplier_list.append(supplierinfo)
            elif userInputSupplier == 3:
                File_Handling.save_supplier(supplier_list)
                break

    elif userInput == 8:
        inside_order_loop = True
        while inside_order_loop == True:
            print(
                "\n----------- MENU -----------\n"
                "1. View Orders\n"
                "2. Create Order\n"
                "3. Add Product to Order\n"
                "4. Calculate Order\n"
                "5. Save and Exit\n"
                "----------------------------\n"
            )
            userInputOrder = Main_Program.get_valid_order_input()
            if userInputOrder == 1:
                print("---------- Orders ------------")
                if len(orderlist) == 0:
                    print("There are no orders.")
                else:
                    for order in orderlist:
                        print("\nOrder ID:", order.order_id)
                        order.display_order()

            elif userInputOrder == 2:
                order_id_list=Main_Program.get_order_id_list(orderlist)
                Main_Program.get_order_input(order_id_list,orderlist)

            elif userInputOrder == 3:
                order_id_list=Main_Program.get_order_id_list(orderlist)
                Main_Program.get_product_add_order(order_id_list,orderlist,current_inventory)
                
            elif userInputOrder == 5:
                File_Handling.save_order(orderlist)
                break