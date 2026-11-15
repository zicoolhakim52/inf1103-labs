import json
from DigitalProduct import DigitalProduct
from Order import Order
from OrderLine import OrderLine
from PhysicalProduct import PhysicalProduct
from Product import Product
from Supplier import Supplier


class File_Handling:

    def load_inventory(inventoryQuantity):
        try:
            inventoryFile = open("inventory.json", "r+")
            inventoryFile.close()
            print("inventory.json found.")

            with open("inventory.json", "r") as file:
                file_contents = json.load(file)

            for item in file_contents:
                inventoryQuantity += int(item["Stock"])

            lastItem = file_contents[-1]
            lastItemID = lastItem["ID"]
            lastItemID = int(lastItemID[-1])

            print("Inventory loaded successfully.\n")
            return [file_contents, inventoryQuantity, lastItemID]

        except:
            inventoryFile = open("inventory.json", "w+")
            inventoryFile.close()
            return "Empty"

    def save_inventory(current_inventory, state):
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
            return file_contents
        except:
            return []

    def save_supplier(unique_supplier):
        supplier_list = []
        for supplier in unique_supplier:
            supplier_list.append(supplier.save_supplier())
        with open("supplier.json", "w+") as file:
            json.dump(supplier_list, file, indent=1)

    def load_order(current_inventory) -> list[Order] | None:
        try:
            with open("order.json", "r") as file:
                file_contents = json.load(file)
            order_list = []
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

            return order_list
        except:
            orderFile = open("order.json", "w+")
            orderFile.close()

    def save_order(orderlist):
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