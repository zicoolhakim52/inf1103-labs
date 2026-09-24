#Functions

#gets quantity of user input and validates it
def get_valid_input():


    inputStrList=["Enter Product Name: ", "Enter Quantity: "]
    errorMsgList=["Please enter a valid Product Name or 'quit' to exit: ", "Please enter a valid quantity or 'quit' to exit: "]
    inputList=[]
    #variable holds command
    for index in range(2):    #for loop for the the two items in the list [product name, quantity]
        userInput = input(inputStrList[index])
        #Selects the corresponding boolean condition based on the index
        if index==0:
            inputCondition=userInput.isalpha() == False
        else:
            inputCondition=userInput.isdigit() == False

        while inputCondition and userInput !="quit":
            #how to count invalid input
            print("Invalid input")
            userInput = input(errorMsgList[index])  
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
def load_inventory():
    try:
        inventoryFile= open("inventory.txt",'r+')
    except:
        inventoryFile= open("inventory.txt",'w+')
    #closes file
    inventoryFile.close()

    ##Reads data from file
    with open("inventory.txt",'r+') as file:
        data_output = file.readlines()
    return(data_output)



#variable holds inventory quantity
inventoryQ = 0
#List of new input in this session
sessionInputList=[]
##loads inventory
loaded_inventory=load_inventory()

#get inventory number of last items
for eachOrder in loaded_inventory:
    tempSplit=eachOrder.split(",")
    #Adds all the inventory quantity from list
    inventoryQ+=int(tempSplit[-1])

#Gets the last item from the inventory.txt
lastItem=loaded_inventory[-1]
lastItem=lastItem.split(",")
#Get the order number of the last item on the list
lastItemNumber=lastItem[0]




while True:
    if inventoryQ < 500:
        userInput= get_valid_input()
        #checks if the total inventory will be more than 500
        if userInput != "quit":
            intentoryCheck=inventoryQ
            intentoryCheck+=int(userInput[1])
    else:
        #trigger overstock alert
        userInput="quit"
        print("\nALERT! Inventory limit reached.\nNo more stock can be added")
    #The only break condition to exit while loop
    if userInput== "quit":
        print("Total Tax on delivery is: ", calculate_tax(inventoryQ))
        Rcount=errorCount()
        generate_report(inventoryQ,Rcount-1)
        print(sessionInputList)
        #Writes new inputs to file
        with open("inventory.txt",'r+') as file:
            for index in len(sessionInputList):
                file.write(str(int(lastItemNumber)+index)+", "+str(sessionInputList[index][0])+", "+str(sessionInputList[index][1])+"\n")
        break
    else:
        if intentoryCheck >500:
            print("Stock not added. Current Inventory would be more than 500: ", intentoryCheck) 
        else:
            inventoryQ=process_delivery(inventoryQ,int(userInput[1]))
            print("Stock added. Current Inventory: ", inventoryQ)
            ##adds the valid input into the list
            sessionInputList.append(userInput)

            
    



