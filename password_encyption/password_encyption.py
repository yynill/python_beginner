from cryptography.fernet import Fernet
import os
file_path = os.path.join(
    './password_encyption/', 'password_encyption.txt')


# key is generated - not needed anymore.
# def write_key():
#    key = Fernet.generate_key()
#    with open("key.key", "wb") as key_file:
#        key_file.write(key)


def load_key():
    file = open("./password_encyption/key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pasword = "master"
master_pasword_input = input("Enter master Password: ")
key = load_key()
'''+ master_pasword.encode()'''
fer = Fernet(key)


while True:
    action = input('''
Actions:
--------
Create Password (c)?
View Passwords (v)?
quit programm (q)?
> ''').lower()

    with open(file_path, 'r') as p:
        lines = p.readlines()

    with open(file_path, 'r') as p:
        all = p.read()

    if action == 'c':
        pos_new = int(len(lines)+1)
        new_user = input(f'Enter new user name ({pos_new})> ')
        new_password = input(f'Enter new password # {pos_new}> ')
        with open(file_path, 'a') as p:
            p.write(
                f'password_{pos_new}-{new_user}-{fer.encrypt(new_password.encode())}'
                + '\n')
            print(f'password # {pos_new} created...')

    elif action == 'v':
        print('''--------------------
    # for single password
    0 - for all passwords
    --------------------''')
        line_number = int(input('password # '))

        if 1 <= line_number <= len(lines):
            line_to_read = lines[line_number - 1]
            passw_id, user, passw = line_to_read.split("/-/")

            print(
                f'User: {user} Password: {fer.decrypt(passw.encode()).decode()}'
            )
        elif line_number == 0:
            print(all)
        else:
            print(f'No Password # {line_number} found.')

    elif action == 'q':
        break

    else:
        print('command not found!')
