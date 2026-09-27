import random

# this only will give you 5 and if you want to change you need to change the number as well
# number_of_dice = 5

# track whether we still need to keep asking the user for a valid number
asking_for_input = True

# main validation loops: keeps repeating until the user gives a valid answer
while asking_for_input:

    # ask for input as plain text first so the program does not crash on letters
    user_text = input('How many dice would you like to roll? ')

    # check if the text is only made digits and is greater than zero
    # .isdigit() prevents crashes if the user accidentally typed letters
    if user_text.isdigit() and int(user_text) > 0:

        # if valid, safely convert it to  an integer using your variable name
        number_of_dice = int(user_text)

        # turn the loop condition to false to stop the while loop
        asking_for_input = False

    else:
        # if they typed letters, a zero, or a negative number, show an error
        # the loop will automatically start over and ask again
        print('Error: Please enter a whole number that is 1 or greater!\n')


# print('About to roll ' + str(number_of_dice) + 'dice') # same

# it's called format string or f string
print(f'About to roll {number_of_dice} dice.') # same

# gives you random numbers again and again but won't reach 6 numbers
for dice in range(number_of_dice): # roll 5 dice

    # pick a random number between 1 and 6
    dice_value = random.randint(1, 6) # just 1-5 but different

   # print('Dice ' + str(dice) + ' value is ' + str(dice_value)) # same
    print(f'Dice {dice+1} value is {dice_value}') # using f string (same)