from DigitalProduct import DigitalProduct
from File_Handling import File_Handling
from Inventory import Inventory
from Main_Program import Main_Program
from Order import Order
from PhysicalProduct import PhysicalProduct
from Supplier import Supplier


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
    if product_type == "Digital":
        download_size_input = Main_Program.get_valid_digital_input()
        product = DigitalProduct(
            search_item,
            productName,
            productPrice,
            stockQuantity,
            download_size_input,
            supplierinfo,
        )
    else:
        product_weight_input = Main_Program.get_valid_weight_input()
        product = PhysicalProduct(
            search_item,
            productName,
            productPrice,
            stockQuantity,
            product_weight_input,
            supplierinfo,
        )
    return product


def order_exists(orderlist: list, orderID: str) -> Order | bool:
    for order in orderlist:
        if str(orderID) == str(order.order_id):
            print("Order Found")
            return order
    print("Order Not Found. Please Enter a valid ID")
    return False


print(
    "======================================== \n"
    "INVENTORY MANAGEMENT SYSTEM\n"
    "========================================"
)
inventoryQuantity = 0
lastItemNumber = 0
current_inventory = Inventory()
supplier_list = []

loaded_inventory = File_Handling.load_inventory(inventoryQuantity)

if loaded_inventory != "Empty":
    for item in loaded_inventory[0]:
        supplier_info = Supplier(
            item["SupplierID"], item["SupplierName"], item["SupplierEmail"]
        )
        if "Download size" in item.keys():
            product = DigitalProduct(
                item["ID"],
                item["Name"],
                item["Price"],
                item["Stock"],
                item["Download size"],
                supplier_info,
            )
        else:
            product = PhysicalProduct(
                item["ID"],
                item["Name"],
                item["Price"],
                item["Stock"],
                item["Weight"],
                supplier_info,
            )
        current_inventory.add_product(product)
    inventoryQuantity = int(loaded_inventory[1])
    lastItemNumber = int(loaded_inventory[2])

supplier_load = File_Handling.load_supplier()
if len(supplier_load) != 0:
    for supplier in supplier_load:
        supplier_info = Supplier(
            supplier["SupplierID"],
            supplier["SupplierName"],
            supplier["SupplierEmail"],
        )
        supplier_list.append(supplier_info)

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
        supplierID = input("Enter Supplier ID: ")
        supplierName = input("Enter Supplier Name: ")
        supplierEmail = input("Enter Supplier Email: ")
        supplierinfo = Supplier(supplierID, supplierName, supplierEmail)
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
        inventoryQuantity = inventoryQuantity + int(new_stock) - int(old_stock)
        result = stockOverflow(inventoryQuantity)
        if result == True:
            item["Stock"] = new_stock
            product_info.update_stock(new_stock)
            print("\nStock updated successfully!\n")
        else:
            inventoryQuantity = inventoryQuantity - int(new_stock) + int(old_stock)
            print("Quantity would go over 500. Item not added")

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
                if len(supplier_list) != 0:
                    for supplier in supplier_list:
                        supplier.display_information()
                        print("\n")
                else:
                    print("There are no suppliers information available")
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
                print("---------- Orders ------------\n")
                if len(orderlist) == 0:
                    print("There are no orders.")
                else:
                    for order in orderlist:
                        print("\nOrder ID:", order.order_id)
                        order.display_order()
            elif userInputOrder == 2:
                order_ID = input("Enter Order ID: ")
                order = Order(order_ID)
                orderlist.append(order)
            elif userInputOrder == 3:
                userInputOrderID = input("Enter an order ID: ")
                order = order_exists(orderlist, userInputOrderID)
                if order != False:
                    product = Main_Program.get_input_ID(0, current_inventory)
                    quantity = input("Please enter quantity: ")
                    order.add_order_line(product, quantity)
                    print("Product added!")
                else:
                    print("Product not added")
            elif userInputOrder == 5:
                File_Handling.save_order(orderlist)
                break