import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

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
            if symbol_to_check != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winning_lines,winnings

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|",end=" ")
            else:
                print(column[row],end=" ")
        print("\n")
        
def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount >=0:
                break
        else:
            print("Enter a valid amount.")
    return amount
def get_number_of_lines():
    while True:
        lines = input("Enter the amount of lines you want to bet on (1-"+ str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if lines >0 and lines <= MAX_LINES:
                break
            else:
                print("Enter a valid amount.")
        else:
            print("Enter a valid amount.")
    return lines
def get_bet():
    while True:
        amount = input("Enter the amount you want to bet on each line: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <=amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Enter a valid amount.")
    return amount
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f"You don't have enough balance to make this bet.Your current balance is ${balance}.")
        else:
            break

    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    while True:
        play = input("Do you want to spin the slot machine? (Y/N): ")
        if play.lower() == "y":
            break
        elif play.lower() == "n":
            print("You have ended the game.")
            return 0
        else:
            print("Enter a valid input.")
    slots=get_slot_machine_spin(ROWS, COLS, symbol_count)
    winning_lines, winnings = check_winnings(slots, lines, bet, symbol_value)
    balance += winnings - total_bet
    print_slot_machine(slots)
    print(f"You won ${winnings}!")
    print(f"You won on", *winning_lines)
    return winnings-total_bet

def main():
    f = open("balance.txt", "r+")
    balance = int(f.read())
    print(f"Current balance is ${balance}")
    balance+=deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit):")
        if answer.lower() == "q":
            print(f"Your final balance is ${balance}")
            f.seek(0)
            f.write(str(balance))
            break
        balance+=spin(balance)
    
main()
