import random
# Deposit - Only Numbers Valid
while True:
    try:
        deposit = input('Deposit amount: $')
        deposit = int(deposit)
        balance = deposit
        print(f'Current Balance: ${balance} \n')
        break
    except ValueError:
        print('Invalid input. Please enter a valid number.\n')


def set_slot(lines, bet_size):
    char = ["A", "B", "C", "D", "E"]
    slot_Machine = []
    for _ in range(3):
        row = []
        for _ in range(3):
            single = random.choice(char)
            row.append(single)
        slot_Machine.append(row)

    print(f'''
{slot_Machine[0][0]} | {slot_Machine[0][1]} | {slot_Machine[0][2]}          <-- Line 1
---------
{slot_Machine[1][0]} | {slot_Machine[1][1]} | {slot_Machine[1][2]}          <-- Line 2
---------
{slot_Machine[2][0]} | {slot_Machine[2][1]} | {slot_Machine[2][2]}          <-- Line 3
''')

# calc win loss


def set_bet():
    lines = input('How many lines do you want to bet on (1-3)? ')
    bet_size = input('What would you want to bet on each line? $')
    return lines, bet_size


def start_slot():
    lines, bet_size = set_bet()
    total_bet = int(lines) * int(bet_size)
    print(f'Your Bet: {lines} Lines each ${bet_size} ==> Total: ${total_bet}')
    set_slot(lines, bet_size)


while True:
    menu = input('\nPress Enter to Play || Quit with (q)').lower()
    if menu != "q":
        start_slot()
    elif menu == "q":
        break
