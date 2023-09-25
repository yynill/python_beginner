import random
# Deposit - Only Numbers Valid


def get_deposit():
    while True:
        try:
            amount = int(input('Deposit amount: $'))
            return amount
        except ValueError:
            print('Invalid input. Please enter a valid number.\n')


def set_slot(lines, bet_size, deposit):
    char = ["A", "B", "C"]
    slot_Machine = []
    for _ in range(3):
        row = []
        for _ in range(3):
            single = random.choice(char)
            row.append(single)
        slot_Machine.append(row)

    print(f'''
{slot_Machine[0][0]} | {slot_Machine[0][1]} | {slot_Machine[0][2]}          <-- Line 0
---------
{slot_Machine[1][0]} | {slot_Machine[1][1]} | {slot_Machine[1][2]}          <-- Line 1
---------
{slot_Machine[2][0]} | {slot_Machine[2][1]} | {slot_Machine[2][2]}          <-- Line 2
''')

    # calc win loss

    # check if line won:
    count_winning_rows = []
    for i in range(3):
        if slot_Machine[i][0] == slot_Machine[i][1] and slot_Machine[i][1] == slot_Machine[i][2]:
            count_winning_rows.append(i)

    win = len(count_winning_rows) * (bet_size * 2)
    loss = bet_size * lines

    total = win - loss

    print(f'''
You won: ${win}
On lines: {count_winning_rows}''')
    return total


deposit = get_deposit()

while True:
    menu = input('\nPress Enter to Play || Quit with (q)').lower()
    if menu != "q":
        lines = int(input('How many lines do you want to bet on (1-3)? '))
        bet_size = int(input('What would you want to bet on each line? $'))

        total_bet = lines * bet_size
        print(
            f'Your Bet: {lines} Lines each ${bet_size} ==> Total: ${total_bet}')
        deposit += set_slot(lines, bet_size, deposit)
        print(f'Current Balance: ${deposit}')
    elif menu == "q":
        print(f'\nCashout: {deposit}')
        break
