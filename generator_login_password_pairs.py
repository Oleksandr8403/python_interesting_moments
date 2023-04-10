import random
'''In this file, we exercise how to use dict comprehension for applied tasks'''


def users_passwords(count):
    symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    users_passwords_dict = {
        f'user{x}': f'{random.choice(symbols)}{random.choice(symbols)}{random.choice(symbols)}'
                    f'{random.choice(symbols)}{random.choice(symbols)}{random.choice(symbols)}'
                    f'{random.choice(symbols)}{random.choice(symbols)}{random.choice(symbols)}'
                    f'{random.choice(symbols)}{random.choice(symbols)}{random.choice(symbols)}'
                    f'{random.choice(symbols)}{random.choice(symbols)}{random.choice(symbols)}'
                    for x in range(1, count+1)
    }

    for key, value in users_passwords_dict.items():
        print(key, value)
    return users_passwords_dict


if __name__ == '__main__':
    users_passwords(int(input('Please enter a number of user-password pairs\n')))
