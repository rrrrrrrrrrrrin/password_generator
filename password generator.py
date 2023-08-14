from random import *

digits, letters, punctuation, vague_symbols = '0123456789', 'abcdefghijklmnopqrstuvwxyz',\
                                              '!#$%&*+-=?@^_', 'il1Io0O'
counter = 0
chars = ''


def generate_password(length, chars):
    password = ''
    for _ in range(int(length)):
        password += choice(chars)
    print(password)


while True:
    amount = input('How many passwords would you like to generate?: ')
    if amount.isdigit():

        for i in [digits, letters, letters.upper(), punctuation]:
            if input(f'Will your passwords include {i}? (y/n): ') == 'y':
                counter += 1
                chars += i

        if input(f'Exclude the vague symbols {vague_symbols}? (y/n): ') == 'y':
            [chars.replace(i, '') for i in vague_symbols]

        while True:
            length = input('What length do you want your passwords to have?: ')
            if length.isdigit() and int(length) >= counter:

                for _ in range(int(amount)):
                    generate_password(length, chars)

                break
            else:
                print('Either enter a number or your password length'
                      ' is less than the amount of symbols you want to include')
                continue

        break
    else:
        print('Enter a number')
        continue
