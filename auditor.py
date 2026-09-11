
#variable holds inventory
inventory = 0
#variable holds command
userInput = input("Please enter a valid number or 'quit' to exit: ")
#Rejected entries count
Rcount=0


while userInput != "quit":

    #Handles invalid input, enforce buisness rules
    if userInput.isdigit() == False: 
        Rcount+=1
        userInput = input("\nInvalid input. Please enter a valid number or 'quit' to exit: ")     
    else:
        #running total of inventory
        inventory += int(userInput)
        print("Current inventory: ", inventory)
        if inventory > 500:
            #trigger overstock alert
            print("\nALERT! Inventory limit reached.\nNo more stock can be added")
            break
        userInput = input("\nInput accepted. Please enter a valid number or 'quit' to exit: ")


print("\nYou have exited the inventory management system.")
print("Total units processed: ", inventory)
print("Total rejected entries: ", Rcount)
