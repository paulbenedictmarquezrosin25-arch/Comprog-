# if = Do some code if only IF some condition is True
#      Else do something else

age = int(input("Enter your age: "))
# in here, the user is asked to state his/her age. if age is below 18, user will only be selled with juice or water. if above 18, user will have access to different kinds of liquor

if age >= 18:
   print("Welcome to the Bar!")

   drink = input("What drink would you like to purchase (Beer, Orange Juice, Tequila, Water, Whiskey, or Vodka)? ").capitalize()
   if drink == "Beer":
    beer1 = int(input("How many would you like to avail? "))
    total = beer1 * .99
   elif drink == "Orange Juice":
    orj = int(input("How many would you like to avail? "))
    total = orj * .99
   elif drink == "Tequila":
    teq = int(input("How many would you like to avail? "))
    total = teq * 1.67
   elif drink == "Water":
    wat = int(input("How many would you like to avail? "))
    total = wat * .45
   elif drink == "Whiskey":
    whisk = int(input("How many would you like to avail? "))
    total = whisk * 1.99
   elif drink == "Vodka":
    vod = int(input("How many would you like to avail? "))
    total = vod * .50
   
   print(f"That would be ${total} in total. Thank you!")
elif age < 18:
    print("Hey kiddo, welcome to the Bar! Where's your momma? ")

    drink = input("What drink would you like to purchase (Orange Juice or Water)? ")
    if drink == "Orange Juice":
     orj = int(input("How many would you like to avail? "))
     total = orj * .99
    elif drink == "Water":
     wat = int(input("How many would you like to avail? "))
     total = wat * .45

    print(f"That would be ${total} in total. Thank you!")
else:
    print("Sorry, we don't carry that drink.")
    exit()