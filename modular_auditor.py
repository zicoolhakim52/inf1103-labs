#Functions
#gets user input and validates it
def get_valid_input():
    #variable holds command
    userInput = input("Please enter a valid number or 'quit' to exit: ")

    while userInput.isdigit() == False and userInput !="quit":
        #how to count invalid input
        print("Invalid input")
        userInput = input("Please enter a valid number or 'quit' to exit: ")  
        #Keep track of number of errors
        errorCount()
    #Handles invalid input, enforce buisness rules
    if userInput=="quit":
        return("quit")
    #elif userInput.isdigit() == False:
     #   return("invalid")
    else:
        return(userInput)
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

#variable holds inventory
inventory = 0


while True:
    if inventory < 500:
        userInput= get_valid_input()
        #checks if the total inventory will be more than 500
        if userInput != "quit":
            intentoryCheck=inventory
            intentoryCheck+=int(userInput)
    else:
        #trigger overstock alert
        userInput="quit"
        print("\nALERT! Inventory limit reached.\nNo more stock can be added")
    #The only break condition to exit while loop
    if userInput== "quit":
        print("Total Tax on delivery is: ", calculate_tax(inventory))
        Rcount=errorCount()
        generate_report(inventory,Rcount-1)
        break
    else:
        if intentoryCheck >500:
            print("Stock not added. Current Inventory would be more than 500: ", intentoryCheck) 
        else:
            inventory=process_delivery(inventory,int(userInput))
            print("Stock added. Current Inventory: ", inventory)            
            
                



