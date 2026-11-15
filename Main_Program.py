from Supplier import Supplier
from Order import Order
from DiscountStrategy import DiscountStrategy
from BulkDiscount import BulkDiscount
from NoDiscount import NoDiscount
from PercentageDiscount import PercentageDiscount
from StudentDiscount import StudentDiscount
from Product import Product
class Main_Program:

    def display_menu():
        print(
            "----------- MENU -----------\n"
            "1. Display All Products\n"
            "2. Add Product\n"
            "3. Update Stock\n"
            "4. Search Product\n"
            "5. Save Inventory\n"
            "6. Exit\n"
            "7. Suppliers\n"
            "8. Order\n"
            "----------------------------\n"
        )

    def get_valid_input()->str:
        input_Option = ""
        while type(input_Option) != int:
            try:
                input_Option = int(input("Enter option: "))
                if input_Option not in [1, 2, 3, 4, 5, 6, 7, 8]:
                    print("Invalid option, Please type an option that is displayed")
            except:
                print("Invalid option, Please type an option that is displayed")
                continue
        return input_Option

    def get_valid_supplier_input()-> str:
        input_Option = ""
        while type(input_Option) != int:
            try:
                input_Option = int(input("Enter option: "))
                if input_Option not in [1, 2, 3]:
                    print("Invalid option, Please type an option that is displayed")
            except:
                print("Invalid option, Please type an option that is displayed")
                continue
        return input_Option

    def get_valid_order_input()->str:
        input_Option = ""
        while type(input_Option) != int:
            try:
                input_Option = int(input("Enter option: "))
                if input_Option not in [1, 2, 3, 4, 5, 6]:
                    print("Invalid option, Please type an option that is displayed")
            except:
                print("Invalid option, Please type an option that is displayed")
                continue
        return input_Option

    def get_input_ID(userInput, current_inventory)-> bool | Product:
        validateInputID = False
        while validateInputID == False:
            current_inventory.display_all()
            search_item = input("Product ID: ")
            validateInput = Main_Program.validateID(search_item)
            if validateInput:
                IDExistsCheck = Main_Program.IDExists(
                    search_item, current_inventory, userInput
                )
                if IDExistsCheck != None:
                    if userInput == 2:
                        print("ID already exists, Please enter another ID")
                    else:
                        validateInputID = True
                        return IDExistsCheck
                else:
                    if userInput == 2:
                        return search_item
                    else:
                        print("ID does not exists, Please enter another ID")

    def validateID(productID)->bool:
        if productID == "":
            print("Product ID cannot be empty")
            return False
        else:
            first_letter = productID[0]
            if first_letter != "P":
                print("Product ID must start with P (case sensitive)")
                return False
            elif len(productID) != 4:
                print(
                    "Product ID must be 4 letters long. e.g. Pxxx where x is an integer"
                )
                return False
            else:
                three_digits = productID[1:3]
                if three_digits.isdigit():
                    return True
                else:
                    print("Please input Pxxx where x is an integer")
                    return False

    def IDExists(ID, current_inventory, userInput)->None | Product:
        search_result = current_inventory.search_product_by_ID(ID, userInput)
        if search_result == None:
            return None
        else:
            return search_result

    def add_product(productID, current_inventory)-> None:
        validation = Main_Program.validateID(productID)
        if validation:
            ID = Main_Program.IDExists(productID, current_inventory, 0)
            if ID != None:
                return ID
            else:
                print("ID does not exists, Please enter another ID")


    def get_product_type()-> str:
        product_type = ""
        while True:
            product_type = input("Input product type: physical or digital: ")
            if product_type.lower() != "physical" and product_type.lower() != "digital": 
                print("Please enter physical or digital.")
            else:
                break
        return product_type

    def get_product_price()-> float:
        validateInputPrice = False
        while validateInputPrice == False:
            productPrice = input("Price: ")
            if float(productPrice) >0 and productPrice.isdigit():
                validateInputPrice = True
            else:
                print("Price must be a int/float and more than 0. e.g. 12.50")
        return productPrice

    def get_valid_stock()-> int:
        validateInputStock = False
        while validateInputStock == False:
            stockQuantity = input("Stock Quantity: ")
            if stockQuantity.isdigit() and int(stockQuantity)>0:
                validateInputStock = True
            else:
                print("Stock must be an integer and more than 0. e.g. 10")
        return stockQuantity

    def get_valid_digital_input()-> float:
        download_size_input = False
        while type(download_size_input) != float:
            download_size_input = input("Download file size in (GB): ")
            try:
                download_size_input = float(download_size_input)
            except:
                print("Error: The input is not a valid float.")
        return download_size_input

    def get_valid_weight_input()-> float:
        product_weight_input = False
        while type(product_weight_input) != float:
            product_weight_input = input("Enter weight of product in KG: ")
            try:
                product_weight_input = float(product_weight_input)
            except:
                print("Error: The input is not a valid float.")
        return product_weight_input

    def get_supplier_list(supplier_list)-> None:
        if len(supplier_list) != 0:
            for supplier in supplier_list:
                supplier.display_information()
                print("\n")
        else:
            print("There are no suppliers information available")
    def get_supplier_id_list(supplier_list:list) -> list | None:
        if len(supplier_list) != 0:
            supplier_id_list=[]
            for supplier in supplier_list:
                supplier_id_list.append(supplier.get_supplier_id())
            return supplier_id_list
        else:
            print("There are no suppliers information available")        

    def get_supplier_by_id(supplierID,supplier_list) -> Supplier:
        for supplier in supplier_list:
            if supplierID== supplier.get_supplier_id():
                break
        return supplier

    def input_supplier_id(supplier_id_list:list,supplier_list:list)-> None:
        while True:
            try:
                supplierID = input("Enter Supplier ID: ")
            except int(supplierID)<0 or supplierID.isdigit() or supplierID not in supplier_id_list():
                print("Please select a digit whitin the range of supplier ID")
            else:
                supplierinfo = Main_Program.get_supplier_by_id(supplierID,supplier_list)
                break
            
        return supplierinfo

    def get_order_id_list(orderlist)-> list:
        order_id_list=[]
        for order in orderlist:
            order_id_list.append(order.get_id())
        return order_id_list

    def get_order_input(order_id_list,orderlist)-> None:
        while True:
            order_ID = input("Enter Order ID: ")
            if not order_ID.isdigit():
                print("ID must be a digit (1,2,3...)")
            elif int(order_ID)<=0:
                print("ID cannot be 0 or negative number")
            elif order_ID in order_id_list:
                print("ID already exists, please select another ID")
            else:
                order = Order(order_ID)
                orderlist.append(order)
                break
    
    def order_exists(orderlist: list, orderID: str) -> Order | bool:
        for order in orderlist:
            if str(orderID) == str(order.order_id):
                print("Order Found")
                return order
        print("Order Not Found. Please Enter a valid ID")
        return False
    def get_product_add_order(order_id_list,orderlist,current_inventory)-> None:
        while True:
            order_id_list.append('0')
            userInputOrderID = input("Enter an order ID (or enter 0 to exit): ")
            if not userInputOrderID.isdigit():
                print("Input must be digit")
            elif userInputOrderID not in order_id_list:
                print("Order Does not exist")
            elif int(userInputOrderID)!=0:
                order = Main_Program.order_exists(orderlist, userInputOrderID)
                if order != False:
                    product = Main_Program.get_input_ID(0, current_inventory)
                    quantity = input("Please enter quantity: ")
                    order.add_order_line(product, quantity)
                    print("Product added!")
                    break
                else:
                    print("Product not added")
            else:
                print("Exited")
                break

    def set_order_discount(order_id_list,orderlist)->None:
        while True:
            order_id_list.append('0')
            userInputOrderID = input("Enter an order ID (or enter 0 to exit): ")
            if not userInputOrderID.isdigit():
                print("Input must be digit")
            elif userInputOrderID not in order_id_list:
                print("Order Does not exist")
            elif int(userInputOrderID)!=0:
                order = Main_Program.order_exists(orderlist, userInputOrderID)
                print("----------Discounts----------\n")
                print("1.No discount\n2.Bulk Discount\n3.Percentage Discount\n4.Student Discount")
                discount_range=[0,1,2,3,4]
                discount_strat=[NoDiscount(),BulkDiscount(),PercentageDiscount(0.1),StudentDiscount()]
                inputvalid=True
                break
                
            else:
                print("Exited")
                inputvalid=False
                break

        while inputvalid:
            discount_input = input("Enter Discount (or 0 to exit): ")
            if not discount_input.isdigit():
                print("Not a number. Please enter a digit from 1-4")
            elif int(discount_input) not in discount_range:
                print("Out of range. Please enter a digit from 1-4")
            elif discount_input=="0":
                print("Exited")
                break
            else:
                order.set_discount(discount_strat[int(discount_input)-1])
                break
            
    def calulateOrder(order_id_list,orderlist) -> None:
        while True:
            order_id_list.append('0')
            userInputOrderID = input("Enter an order ID (or enter 0 to exit): ")
            if not userInputOrderID.isdigit():
                print("Input must be digit")
            elif userInputOrderID not in order_id_list:
                print("Order Does not exist")
            elif int(userInputOrderID)!=0:
                order = Main_Program.order_exists(orderlist, userInputOrderID)
                price=order.calculate_total()
                print(f"Total price for {order.get_id()} is {price}")
                break
                
            else:
                print("Exited")
                break
                
            
            
