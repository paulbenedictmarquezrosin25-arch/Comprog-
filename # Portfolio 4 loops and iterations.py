# Portfolio 4_Rosin loops and iterations

# importing of necessary codes for the program to run successfully 
import random
import time

# the possible variables that will be randomly presented in the slot machine
SYMBOLS = ["🍒", "🍋", "🍊", "🔔", "💎"]

# Initialize tracking variables (Loop Idioms)
balance = 50            # the starting balance (100 credits)
total_spins = 0          # counting idiom
total_won = 0            # summing idiom
highest_payout = 0       # finding the largest value idiom

print("=============================================")
print("     Welcome to DaksSino Slots Machine!")
print("     Feeling lucky? Each spin costs ₱5. ")
print("=============================================\n")

# this code will run until either the user runs out of money or decides to quit the game 
while True:
    print(f"Current Balance: ₱{balance}")
    user_input = input("Press ENTER to spin (₱5) or type 'exit' to cash out: ").strip().lower()
    
    # 'break' : Exit if the user chooses to quit
    if user_input == "exit":
        print("\nCashing out your chips...")
        break
        
    # check if user has enough money
    if balance < 5:
        print("\nYou don't have enough money left to spin! Game over.")
        break
        
    # deduct the cost of the spin
    balance = balance - 5
    total_spins = total_spins + 1 
    print("\n[ Spinning... ]")
    time.sleep(0.5)
    
    # code that runs exactly 3 times to generate 3 reels
    current_spin_result = []
    for i in [1, 2, 3]:  # Explicit sequence
        random_symbol = random.choice(SYMBOLS)
        current_spin_result.append(random_symbol)
        
    # display the slot result
    print(f"  | {current_spin_result[0]} | {current_spin_result[1]} | {current_spin_result[2]} |")
    
    # calculate winnings based on results
    spin_winnings = 0
    
    # Logic checking for combinations
    if current_spin_result[0] == current_spin_result[1] == current_spin_result[2]:
        # Jackpots: 3 of a kind
        if current_spin_result[0] == "💎":
            spin_winnings = 100
            print("LAKASSS JACKPOT!!! You hit three Diamonds! You got ₱100! 💎💎💎")
        else:
            spin_winnings = 30
            print("Edi ikaww na! 3 of a kind! You got ₱30!")
            
    elif (current_spin_result[0] == current_spin_result[1]) or \
         (current_spin_result[1] == current_spin_result[2]) or \
         (current_spin_result[0] == current_spin_result[2]):
        # 2 of a kind
        spin_winnings = 10
        print("Sheeshh! 2 of a kind! You got ₱10!")
    else:
        print("Nice try buddy. Better luck next spin!")
        
    # summing up total winnings
    total_won = total_won + spin_winnings
    balance = balance + spin_winnings
    
    # finding the largest value (tracking highest single payout)
    if spin_winnings > highest_payout:
        highest_payout = spin_winnings
        
    print("---------------------------------------------")

# results after the spin ends
print("\n=============================================")
print("             🎰 FINAL SESSION STATS 🎰          ")
print("=============================================")
print(f"Total Spins Played : {total_spins}")
print(f"Total Money Won    : ₱{total_won}")
print(f"Highest Win Spin   : ₱{highest_payout}")
print(f"Final Take-Home Cash: ₱{balance}")

# if user decides to exit or runs out of money
if balance > 100:
    print(f"Profit             : +₱{balance - 100} (Uyyy pabalato naman dyan pre! 🤑)")
elif balance < 100:
    print(f"Loss               : -₱{100 - balance} (Nicee G! Bawi next timee pre!)")
else:
    print("Result             : Broke even! (Ayos lang yan, try again for the win!)")
print("=============================================")