
def dispense_drink(drinkName, drinkCount):
    available_drinks = ["Coke", "Water", "Juice"]
    
    if drinkName in available_drinks:
        drinkCount+=1
        print(drinkCount)
        print(f"Dispensing {drinkName}.")
    else:
        print("Drink not available.") 
    return drinkCount



drinkCount=0
while True:
    drink=input("Enter the drink you want: ")
    drinkCount = dispense_drink(drink, drinkCount)
    print(drinkCount)
    if drink == "exit":
        break

print("You have exited the program")
print("Number of drinks dispense: ", drinkCount)
