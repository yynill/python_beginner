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


def start_slot():
    pass


while True:
    menu = input('Press Enter to Play || Quit with (q)').lower()
    if menu != "q":
        start_slot()
    elif menu == "q":
        break
