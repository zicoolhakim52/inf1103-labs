import json
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