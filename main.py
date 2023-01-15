import random # random module

# global constant
MAX_LINES = 3 # global constant; this value is not going to change
MAX_BET = 100
MIN_BET = 1

# 3 BY 3 SLOT MACHINE
ROWS = 3
COLS = 3

# number of symbols in ea reel
# create a dictionary
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            
    return winnings, winning_lines
    
# generate outcome of symbols
def get_slot_machine_spin(rows, cols, symbols):
    # create a list that conatins all of the symbols available
    # randomly select 3 symbols from this list
    all_symbols = [] # list every symbol in this var 
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol) # append(add) the data inside "symbol" onto the "all_aymbols list"
    
    columns = [] # storing the symbols into the columns / define column list
    for _ in range(cols): # for every column, do everything in this loop 
        column = []
        current_symbols = all_symbols[:] # copies the all_symbols list and stores into current_symbols list
        for _ in range(rows):
            value = random.choice(current_symbols) # picks random value from this list
            current_symbols.remove(value) # removes current value from the list (to prevent re-using a symbol already selected)
            column.append(value) # add this value/symbol to the column
            
        columns.append(column)
        
    return columns

def print_slot_machine(columns):
    # TRANSPOSING
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): # loop through all items inside of columns
            # print value at first row of ths column
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row], end='')
                
        print() # prints a new line
        
"""
    - collect user's deposit
    - add that amount to their balance
    - allow to bet on a line or multiple lines
    - see if they received those lines
    - spin slot machine
    - generate all the individual items on the reels
    - add earnings to balance
    - subtract bet $
"""

# get initial deposit $
# get bet $
def deposit():
    while True: # keep looping through $ amount until valid $ amount / continue to do this until we break out
        amount = input("what would you like to deposit? $")
        if amount.isdigit(): # tells us if this is a valid whole number? (is this a digit?)
            amount = int(amount) # convert into an integer
            if amount > 0: # check if amount is greater than 0
                print(amount) 
                break # if so, break out of this while loop
            else: # else, if it's not greater than zero
                print("amount must be greater than $0")
        else:
            print("please enter a number") # line 17 - a digit was not entered, request a number
    return amount

"""
    deposit() # call the function
"""

"""
    - how many lines to bet on?
    - how much to bet?
    - multiply bet amount by # of lines
"""
def get_number_of_lines():
        while True: # continue to do this until we break outs
            lines = input("enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
            if lines.isdigit():
                lines = int(lines) # convert text(str) from input box and convert to an integer
                if 1 <= lines <= MAX_LINES: # check if lines is greater than 1 and less than constant variable MAX_LINES
                    break # if so, break
                else: 
                    print("enter a valid number of lines")
            else:
                print("please enter a number") 
        return lines
    
def get_bet():
    while True:
        amount = input("how much do you want to bet on each line? $")  
        if amount.isdigit():  
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("please enter a number")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"you do not have enough to bet that amount. your current balance is: ${balance}")
        else:
            break
    
    print(f"you are betting: ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet
        
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
        
    print(f"You left with ${balance}")
 
    
main() # reruns 100the game with updated balance



""" @tech with tim | youtube """