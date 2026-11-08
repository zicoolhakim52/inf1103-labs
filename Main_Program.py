#Input functions in this class
class Main_Program:
    def display_menu():
        print("----------- MENU -----------\n"
        "1. Display All Products\n" 
        "2. Add Product\n" 
        "3. Update Stock\n"
        "4. Search Product\n"
        "5. Save Inventory\n"
        "6. Exit\n"
        "----------------------------\n")
    def get_valid_input():
        #inputStrList=["Enter Product Name: ", "Enter Quantity: "]
        #errorMsgList=["Please enter a valid Product Name or 'quit' to exit: ", "Please enter a valid quantity or 'quit' to exit: "]
        input_Option=""

        while type(input_Option)!=int:
            try:
                input_Option=int(input("Enter option: "))
                if input_Option not in [1,2,3,4,5,6]:
                    print("Invalid option, Please type an option that is displayed")
            except:
                print("Invalid option, Please type an option that is displayed")
                continue
        return(input_Option)
    def get_input_ID(userInput,current_inventory):
        validateInputID=False
        while validateInputID==False:
            current_inventory.display_all()
            search_item= input("Product ID: ")
            validateInput=Main_Program.validateID(search_item)
            #Search if ID already exists
            if validateInput:
                IDExistsCheck=Main_Program.IDExists(search_item,current_inventory,userInput)
                if IDExistsCheck!=None:
                    if userInput==2:
                        print("ID already exists, Please enter another ID")
                    else:
                        validateInputID=True
                        return IDExistsCheck
                else:
                    if userInput==2:
                        return search_item
                    else:
                        print("ID does not exists, Please enter another ID")


    def validateID(productID):
        if productID=="":
            print("Product ID cannot be empty")
            return False
        else:
            first_letter=productID[0]
            if first_letter!="P":
                print("Product ID must start with P (case sensitive)")
                return False
            elif len(productID) != 4:
                print("Product ID must be 4 letters long. e.g. Pxxx where x is an integer")
                return False
            else:
                three_digits=productID[1:3]
                if three_digits.isdigit():
                    return True
                else:
                    print("Please input Pxxx where x is an integer")
                    return False
    def IDExists(ID,current_inventory,userInput):
        search_result=current_inventory.search_product_by_ID(ID,userInput)
        if search_result==None:
            #current_inventory.display_all()
            return None
            
        else:
            #returns
            return search_result

    def validatePriceType(productPrice):
        try:
            productPrice=float(productPrice)
            price=round(productPrice,2)
            return [True,price]
        except:
            print("Price must be a int/float")
            return [False]

    def get_product_type():
        product_type=False
        while product_type !="Physical" and product_type!= "Digital":
            product_type=input("Input product type: Physical or Digital: ")
        return product_type

    def get_product_price():
        validateInputPrice=False
        while validateInputPrice==False:
            productPrice=input("Price: ")
            validateInput=Main_Program.validatePriceType(productPrice)
            if validateInput[0]:
                #price is rounded to 2 decimal places
                productPrice=validateInput[1]
                validateInputPrice=True
        return productPrice

    def get_valid_stock():
        validateInputStock=False
        while validateInputStock==False:
            stockQuantity=input("Stock Quantity: ")
            if stockQuantity.isdigit():
                validateInputStock=True
            else:
                print("Stock must be an integer")
        return stockQuantity

    def get_valid_digital_input():
        download_size_input=False
        while type(download_size_input)!= float:
            download_size_input=input("Download file size in (GB): ")
            try:
                download_size_input = float(download_size_input)
            except:
                print("Error: The input is not a valid float.")
        return download_size_input

    def get_valid_weight_input():
        product_weight_input=False
        while type(product_weight_input)!= float:
            product_weight_input=input("Enter weight of product in KG: ")
            try:
                product_weight_input = float(product_weight_input)
            except:
                print("Error: The input is not a valid float.")
        return product_weight_input