import random

want_to_quit = '' # empty string is always false

while not want_to_quit:
    dice_value = random.randint(1, 6)
    print(f'You rolled a {dice_value}')
    want_to_quit = input('Would you like to roll again, any other key to quit: ')



