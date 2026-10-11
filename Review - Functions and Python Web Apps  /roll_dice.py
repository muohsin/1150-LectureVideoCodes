import random  # This allows Python to generate random numbers, just like rolling a real die.


def main():
    # Ask the user how many dice they want to roll.
    # input() gets the answer as text, so int() converts it into a whole number.
    number_of_dice = int(input('How many dice to roll? '))

    # Call the roll_dice function and send it the number entered by the user.
    # This tells the function how many times it needs to roll a die.
    roll_dice(number_of_dice)

    # Let the user know that the program has finished rolling all the dice.
    print('That was all the dice')


def roll_dice(number_of_dice):
    # Repeat the loop once for each die the user wants to roll.
    # For example, if the user enters 3, the loop runs 3 times.
    for dice_count in range(number_of_dice):

        # Generate a random whole number from 1 to 6.
        # These are the six possible results on a regular six-sided die.
        dice_roll = random.randint(1, 6)

        # Display the result of the current roll.
        # The f-string inserts the random number into the sentence.
        print(f'The dice rolled a {dice_roll}')


# Call the main function to start running the program.
main()