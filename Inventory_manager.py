import json
#Functions

def display_menu():
    print("----------- MENU -----------" \
    "1. Display All Products" \
    "2. Add Product" \
    "3. Update Stock"\
    "4. Search Product"\
    "5. Save Inventory"\
    "6. Exit"\
    "----------------------------")


#gets quantity of user input and validates it
def get_valid_input(loaded_inventory):
    inputStrList=["Enter Product Name: ", "Enter Quantity: "]
    errorMsgList=["Please enter a valid Product Name or 'quit' to exit: ", "Please enter a valid quantity or 'quit' to exit: "]
    inputList=[]
    input_Option=""

    while type(input_Option)!=int:
        input_Option=input("Enter option: ")
        if type(input_Option)!= int and input_Option not in [1,2,3,4,5,6]:
            print("Invalid option, Please type an option that is displayed")

    if input_Option==1:
        if loaded_inventory== "Empty":
            print("Inventory is Empty")

    #variable holds command
    for index in range(2):    #for loop for the the two items in the list [product name, quantity]
        userInput = input(inputStrList[index])
        #Selects the corresponding boolean condition based on the index. 
        #If the input is valid, inputCondition is set False, if invalid, it is set to True
        if index==0:
            inputCondition=not (all(char.isalpha() or char.isspace() for char in userInput))
        else:
            inputCondition=userInput.isdigit() == False

        #Enters the while loop when
        while inputCondition and userInput !="quit":
            #how to count invalid input
            print("Invalid input")
            userInput = input(errorMsgList[index]) 
            if index==0 and userInput.isalpha() == True:
                inputCondition=False
            elif index==1 and userInput.isdigit()==True:
                inputCondition=False
            #Keep track of number of errors
            errorCount()
        #Handles invalid input, enforce buisness rules
        if userInput=="quit":
            return("quit")
        #appends valid input into the list
        inputList.append(userInput)

    return(inputList)  #list would be [product name, quantity]

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

        print("Inventory loaded successfully.")
        return([file_contents,inventoryQuantity,lastItemID])

    except FileNotFoundError:
        inventoryFile= open("inventory.json",'w+')
        #closes file
        inventoryFile.close()
        #empty file
        return("Empty")

#Adds one order at a time
def save_inventory(sessionInputList,lastItemNumber):
    print("New Order Added: ")

    with open("inventory.json",'a') as file:
        #json.dump(file)
        orderNumber=str(int(lastItemNumber)+1)
        itemname=str(sessionInputList[0])
        itemquantity=str(sessionInputList[1])
        print(orderNumber+","+itemname+","+itemquantity+"\n")
        file.write(orderNumber+", "+itemname+", "+itemquantity+"\n")
    print("Order successfully saved to orders.txt")
    
##Start of programs
print("======================================== \n"
"INVENTORY MANAGEMENT SYSTEM\n"
"========================================")
#variable holds inventory quantity
inventoryQuantity = 0
#order number of the last item on the list sets to 1001 if no file created before
lastItemNumber=0
#History of last session
historyInventory=[]

##loads inventory (inventory in list)
loaded_inventory=load_inventory(inventoryQuantity)
print(loaded_inventory)
if loaded_inventory != "Empty":
    historyInventory=loaded_inventory[0]
    inventoryQuantity=int(loaded_inventory[1])
    lastItemNumber=int(loaded_inventory[2])

#main loop 
while True:
    #Prevents adding more than 500 Quantity
    if inventoryQuantity < 500:
        userInput= get_valid_input(loaded_inventory)

        #checks if the total inventory will be more than 500
        if userInput != "quit":
            intentoryCheck=inventoryQuantity
            intentoryCheck+=int(userInput[1])
    else:
        #trigger overstock alert
        userInput="quit"
        print("\nALERT! Inventory limit reached.\nNo more stock can be added")
    #The only break condition to exit while loop
    if userInput== "quit":
        print("Total Tax on delivery is: ", calculate_tax(inventoryQuantity))
        Rcount=errorCount()
        generate_report(inventoryQuantity,Rcount-1)
        break
    else:
        if intentoryCheck >500:
            print("Stock not added. Current Inventory would be more than 500: ", intentoryCheck) 
        else:
            inventoryQuantity=process_delivery(inventoryQuantity,int(userInput[1]))
            #print("Stock added. Current Inventory: ", inventoryQuantity)
            #Saves the new input into the file
            save_inventory(userInput,lastItemNumber)
            #Keep tract of count for Order number.
            lastItemNumber+=1

           

