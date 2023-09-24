while True:
    action = input('''
Actions:
--------
Create Password (c)?
View Passwords (v)?
quit programm (q)?
> ''').lower()

    with open('passwords.txt', 'r') as p:
        lines = p.readlines()

    with open('passwords.txt', 'r') as p:
        all = p.read()

    if action == 'c':
        pos_new = int(len(lines)+1)
        new_user = input(f'Enter new user name ({pos_new})> ')
        new_password = input(f'Enter new password # {pos_new}> ')
        with open('passwords.txt', 'a') as p:
            p.write('\n' + f'password_{pos_new}-{new_user}-{new_password}')
            print(f'password # {pos_new} created...')

    elif action == 'v':
        print('''--------------------
    # for single password
    0 - for all passwords
    --------------------''')
        line_number = int(input('password # '))

        if 1 <= line_number <= len(lines):
            line_to_read = lines[line_number - 1]
            print(line_to_read)
        elif line_number == 0:
            print(all)
        else:
            print(f'No Password # {line_number} found.')

    elif action == 'q':
        break

    else:
        print('command not found!')
