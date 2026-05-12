# Portfolio 1 : Expressions 
# This is a code for applying coding expressions revolving about the stock market. The function of this code is to greet the user then get their username account, which includes 
# their owned stocks and current net worth. The code asks them what service would they like to perform (buy stocks, sell stocks, check 
# current stocks and their current value in the market, etc). in buy stocks functions, it shows them the stocks available and their 
# individual price then ask them the amount of stocks they would like to purchase (this will then reduce their net worth for buying 
# the stocks). for sell stocks, this asks them what stocks would they like to sell and how many and show the amount of money they would 
# gain from selling (this will then increase their net worth after selling). In the owned stocks function, show their current value in 
# the market then prediction on how the trend will go in the coming days

# this function allows my portfolio to have an unpredictable outcome, for which in this case is the trend of the stock market
import random

# Stock market data

# these are the available stocks in the market, and yes they are inspired from famous restaurants here in bicol 
market = { 
    "JABE" : 180, 
    "MCDO" : 250, 
    "CHWK" : 140, 
    "BIGGS" : 130, 
    "INSL" : 320
}

# User Database

#this includes the basic information about the user

user = {
    "username": "",
    "cash": 10000, #starting money
    "portfolio" : {} #owned stocks
}

# Helper Functions

# this includes the codes about calculations, stocks still available, or buy and sell of stocks
def showstocks(): #available stocks 
    print("\n Available Stocks:")
    for stock, price in market.items():
        print(f"{stock}: ₱{price}")

def showportfolio(): #money and stocks owned
    print("\n Your Portfolio:")
    totalvalue = user["cash"]
    
    print(f"\n Cash: ₱{user['cash']}")
    print (f"Net Worth: ₱{totalvalue}")

    if not user["portfolio"]:
        print("You don't currently have owned stocks.")
    else: 
        for stock, qty in user["portfolio"].items():
            currentprice = market[stock]
            value = currentprice * qty
            totalvalue += value
            print(f"{stock}: {qty} shares | Current Value: ₱{value}")


# Market trend

# this includes the code for generating the trend of the stock market, though it is all just based on random result depending on the code

    print("\n Market trend Prediction:")
    for stock in market: 
        change = random.choice(['Uptrend, Downtrend, Stable'])
        print(f"{stock}: {change}")

def buystocks():
    showstocks()
    stock = input("\nWhat stock do you want to buy? ").upper()

    if stock not in market:
        print("Invalid stock.")
        return
         
    try: 
        qty = int(input("How many shares do you want to procure? "))
    except:
        print("Invalid number.")
        return
    

    cost = market[stock] * qty

    if cost > user["cash"]:

        print("Not enough balance.")
        return
    
    user["cash"] -= cost
    user["portfolio"][stock] = user["portfolio"].get(stock, 0) + qty

    print(f"You bought {qty} shares of {stock} for ₱{cost} ")

def sellstocks():
    if not user["portfolio"]:
        print("You currently don't own any stocks.")
        return
    
    print("\nYour stocks:")
    for stock, qty in user["portfolio"].items():
        print(f"{stock}: {qty} shares")

    stock = input("\nWhat stock(s) do you want to sell? ").upper()

    if stock not in user["portfolio"]:
        print("You don't have this stock.")
        return
    
    try:
        qty = int(input("How many stock(s) do you want to sell? "))
    except:
        print("Invalid number.")
        return
    
    if qty > user["portfolio"][stock]:
        print("You don't have enough stock(s)")
        return
    
    profit = market[stock] * qty
    user["cash"] += profit
    user["portfolio"][stock] -= qty

    if user["portfolio"][stock] == 0:
        del user["portfolio"][stock]

    print(f"You sold {qty} share(s) of {stock} for ₱{profit}")

# Main program

#this will include the various inputs of the user interface. Including the username or account name, service would they like to perform (buy stocks, sell stocks, check current stocks and their current value in the market, etc)

print("Welcome to DaksStocks Sim!")

user["username"] = input("Enter your account name: ")
print(f"\nHello, {user['username']}! Starting balance: ₱{user['cash']}")

while True:
    print("\n==============================")
    print("What would you like to do? ")
    print("1 Buy Stocks")
    print("2 Sell Stocks")
    print("3 Check Portfolio")
    print("4 Exit")
    print("==============================")

    choice = input("Enter choice: ")

    if choice == "1":
        buystocks()
    elif choice == "2":
        sellstocks()
    elif choice == "3":
        showportfolio()
    elif choice == "4":
        print("Have a nice day! ")
        break
    else:
        print("Invalid choice.")