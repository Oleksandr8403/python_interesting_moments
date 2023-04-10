from generator_login_password_pairs import users_passwords
import random


def test_users_passwords():
    count = random.choice([x for x in range(50, 101)])
    users_passwords_dict = users_passwords(count)

    # Check that the length of the dictionary is equal to count
    assert len(users_passwords_dict) == count, f'{len(users_passwords_dict)}'

    # Check that each user key has a password value of length 12
    for key, value in users_passwords_dict.items():
        assert len(value) == 15, f'{len(value)}'

    # Check that the password values contain only valid symbols
    symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for value in users_passwords_dict.values():
        for char in value:
            assert char in symbols
