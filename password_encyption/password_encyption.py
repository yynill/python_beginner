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


key = load_key()
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

    if action == 'c':
        pos_new = int(len(lines)+1)

        print(f'Enter new data for Password # {pos_new}: ')
        new_user = input('User: ')
        new_password = input('Password: ')

        with open(file_path, 'a') as p:
            p.write(
                f'password_{pos_new}//-/{new_user}//-/{fer.encrypt(new_password.encode()).decode()}'
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
            parts = line_to_read.split("//-/")

            user = parts[1]
            hashed_password = parts[2]
            decrypted_password = fer.decrypt(hashed_password.encode()).decode()
            print(f'User: {user} - Password: {decrypted_password}')

        elif line_number == 0:
            for line_to_read in lines:
                parts = line_to_read.strip().split("//-/")

                user = parts[1]
                hashed_password = parts[2]
                decrypted_password = fer.decrypt(
                    hashed_password.encode()).decode()
                print(f'User: {user} - Password: {decrypted_password}')

        else:
            print(f'No Password # {line_number} found.')

    elif action == 'q':
        break

    else:
        print('command not found!')
