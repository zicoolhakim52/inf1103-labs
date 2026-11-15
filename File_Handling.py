import json
from Order import Order
from OrderLine import OrderLine
from Product import Product
from Supplier import Supplier
from ProductFactory import ProductFactory
from Inventory import Inventory


class File_Handling:

    def load_inventory(current_inventory)->Inventory:
        try:
            inventoryFile = open("inventory.json", "r+")
            inventoryFile.close()
            print("inventory.json found.")

            with open("inventory.json", "r") as file:
                file_contents = json.load(file)

        except FileNotFoundError: #Will create a file
            print("File not found... Creating a file")
            inventoryFile = open("inventory.json", "w+")
            inventoryFile.close()
            return current_inventory
        except json.JSONDecodeError:
            print("File is empty\n")
        else: #Continue running
            #Reads file
            if bool(file_contents):
                for item in file_contents:
                    supplier_info = Supplier(
                        item["SupplierID"], item["SupplierName"], item["SupplierEmail"]
                    )
                    try:
                        product=ProductFactory.create(item["Type"],item["ID"],item["Name"],float(item["Price"]),int(item["Stock"]),supplier_info,item["uniqueTrait"])
                    except ValueError:
                        print("Unknown product type or a price that is not a number")
                        continue
                    else:
                        current_inventory.add_product(product)
            print("Inventory loaded successfully.\n")
        finally:

            print("Load attempt finished.")
        return current_inventory

    def save_inventory(current_inventory, state)->None:
        if state == "Manual Save":
            print("Saving inventory...")
        else:
            print("Saving inventory before exit...")
        if not current_inventory.inventory_empty():
            with open("inventory.json", "w+") as file:
                json.dump(current_inventory.inventory_list_func(), file, indent=1)

        if state == "Manual Save":
            print("Inventory saved successfully to inventory.json.")
        else:
            print("Inventory saved successfully.\n")

    def load_supplier() -> list[Supplier] | list:
        try:
            with open("supplier.json", "r") as file:
                file_contents = json.load(file)
            
        except FileNotFoundError or json.JSONDecodeError:
            return []
        else:
            supplier_list=[]
            for supplier in file_contents:
                supplier_info = Supplier(
                    supplier["SupplierID"],
                    supplier["SupplierName"],
                    supplier["SupplierEmail"],
                )
                supplier_list.append(supplier_info)
        finally:
            print("Load attempt finished.")
        return supplier_list

    def save_supplier(unique_supplier)->None:
        supplier_list = []
        for supplier in unique_supplier:
            supplier_list.append(supplier.save_supplier())
        with open("supplier.json", "w+") as file:
            json.dump(supplier_list, file, indent=1)

    def load_order(current_inventory) -> list[Order] | None:
        order_list = []
        try:
            with open("order.json", "r") as file:
                file_contents = json.load(file)
        except FileNotFoundError:
            orderFile = open("order.json", "w+")
            orderFile.close()
        except json.JSONDecodeError:
            pass
        else:
            for order in file_contents:
                order1 = Order(order["OrderID"])
                list_order_line = order["OrderLines"]
                for order_line in list_order_line:
                    productID = order_line["productID"]
                    for product in current_inventory.getproducts():
                        if productID == product.getProductID():
                            order1.add_order_line(product, order_line["quantity"])
                            break
                order_list.append(order1)
        finally:
            print("Load attempt finished.")
        return order_list
    def save_order(orderlist)->None:
        formatted_orders = []
        for order in orderlist:
            order_dict = {}
            order_dict["OrderID"] = order.get_id()
            orderLines_list = []
            for orderLines in order.get_order_lines():
                orderLines_list.append(orderLines.output_orderLines())
            order_dict["OrderLines"] = orderLines_list
            formatted_orders.append(order_dict)
        with open("order.json", "w+") as file:
            json.dump(formatted_orders, file, indent=1)