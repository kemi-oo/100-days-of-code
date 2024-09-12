print("Welcome to Nola Creations, we are delighted to have you!")
customer_name = input("What is your name?:\n")
customer_number = input("Please input your number, we'ld like to reach out to you for new mouthwatering pastries\n")
customer_favourites = input("Which of our pastries tickle your fancy?\nMeatpie\nCake\nChin Chin\nEgg Roll\nBuns\nPuff Puff\nChocolate Bread\nDoughnuts")
print(f"You can place your order now {customer_name}")
customer_order = input("What do you want to order?\n")
if customer_order == "Meatpie":
    Bill = 0
    MeatpieQty = input("What quantity would you like?\n1\na pack of 2\na pack of 4\n")
    if MeatpieQty == "1":
        Bill += 800
        print(f"okay {customer_name}!, please pay a sum of:# {Bill} to complete your order")
    elif MeatpieQty == "a pack of 2":
        Bill += 1600
        print(f"okay {customer_name}!, please pay a sum of:# {Bill} to complete your order")
    elif MeatpieQty == "a pack of 4":
        Bill += 2400
        print(f"okay {customer_name}!, please pay a sum of:# {Bill} to complete your order")
    else:
        print(f"Sorry {customer_name}! you have made an invalid order")
if customer_order == "Cake":
    Bill = 0
    CakeSize = input("What size of cake would you like?\nplate cake\nsize 4 cake\nsize 6 cake\nsize 10 cake\n")
    if CakeSize == "plate cake":
        Bill += 2500
        print(f"okay {customer_name}!, please pay a sum of:# {Bill} to complete your order")
    elif CakeSize == "size 4 cake":
        Bill += 5000
        print(f"okay {customer_name}!, please pay a sum of:# {Bill} to complete your order")
    elif CakeSize == "size 6 cake":
        Bill += 7500
        print(f"okay {customer_name}!, please pay a sum of:# {Bill} to complete your order")
    elif CakeSize == "size 10 cake":
        Bill += 12500
        print(f"okay {customer_name}!, please pay a sum of:# {Bill} to complete your order")
    else:
        print(f"Sorry {customer_name}! you have made an invalid order")
if customer_order == "Doughnuts":
    Bill = 0
    DoughnutQty = input("What quantity would you like?\na pack of 2\na pack of 4\na pack of 6\na pack of 8\n")
    if DoughnutQty == "a pack of 2":
        Bill += 1200
        print(f"okay {customer_name}!, please pay a sum of:# {Bill} to complete your order")
    elif DoughnutQty == "a pack of 4":
        Bill += 2400
        print(f"okay {customer_name}!, please pay a sum of:# {Bill} to complete your order")
    elif DoughnutQty == "a pack of 6":
        Bill += 3600
        print(f"okay {customer_name}!, please pay a sum of:# {Bill} to complete your order")
    elif DoughnutQty == "a pack of 8":
        Bill += 4800
        print(f"okay {customer_name}!, please pay a sum of:# {Bill} to complete your order")
    else:
        print(f"Sorry {customer_name}! you have made an invalid order")
else:
    print("you have made an invalid order")

    
        
    
         
