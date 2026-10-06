# Example program: random password generator where the user can enter the
# length of the password they want, for example 8 or 12 characters,
# and the program generates a random password of that length.

import string
import random



def main():
    characters = generate_paaword_characters() # make string of all the choices that could include letters, numbers, symbols
    password_length = get_length_from_user() # user input to get ( and validate) length
    password = generate_password(password_length, characters) # generate the random password
    display_password() # show user the generated password


def generate_paaword_characters():

    # TASK - set up the characters to choose from for the password
    letters = string.ascii_letters + 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # numbers = string.digits  # optional
    # symbols = string.punctuation  # optional - have to be careful to only use allowed symbols
    # symbols = '&$!?@'  # so you could make a string of allowed special characters
    # Optional extra question - why don't passwords allow some special characters? More info: "SQL injection"
    # Optional extra question - why are longer, more complex passwords harder to guess?

    all_characters = letters + numbers + symbols # just for debugging
    return all_characters

def get_length_from_user():

    # TASK Ask user how long password should be
    password_length = int(input('Enter password length: '))
    # optional extra - make sure the data entered is an int, at least 8 and no more than 32
    return password_length

def generate_password(password_length, letters):
    # TASK Random character generation to make password
    password = ''  # start with empty string

    for letter in range(password_length):  # repeat once for each letter needed
        random_letter = random.choice(letters)
        print(random_letter)
        password = password + random_letter


# TASK Show the user the generated password, the result from the program
print('Your password is: ' + password)

main()