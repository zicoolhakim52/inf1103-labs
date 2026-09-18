#Functions
def get_valid_input():
    #variable holds command
    userInput = input("Please enter a valid number or 'quit' to exit: ")
    #Handles invalid input, enforce buisness rules
    if userInput=="quit":
        return("quit")
    elif userInput.isdigit() == False:
        return("invalid")
    else:
        return(userInput)

def process_delivery(current_total, new_value):
    current_total += int(new_value)
    return current_total


#variable holds inventory
inventory = 0

#Rejected entries count
Rcount=0

while True:
    userInput= get_valid_input()
    if userInput== "quit":
        break
    elif userInput == "invalid":
        Rcount+=1
        print("Invalid input")
    else:
        inventory=process_delivery(inventory,int(userInput))
        print("Stock added. Current Inventory: ", inventory)
        if inventory > 500:
            #trigger overstock alert
            print("\nALERT! Inventory limit reached.\nNo more stock can be added")
            break    


print("\nYou have exited the inventory management system.")
print("Total units processed: ", inventory)
print("Total rejected entries: ", Rcount)
