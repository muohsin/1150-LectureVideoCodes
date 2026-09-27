# ask the user to enter their weight and convert it to a decimal number
# input ask the user to type something
weight = float(input('Please enter your weight in pounds: '))

# ask the user to enter their age and convert the input to an integer
# ask the user to type something again
age = int(input('Please enter your age in years: '))

# ask how many days ago the user last donated a blood
# the user enters 0 if they have never donated a blood
days_since_donation = int(input('How many days ago did you last donated blood? Enter 0 if you have never donated: '))


# check if the user weights at leats 110 pounds
# is at leat 16 years old, and has waited 56 days between donations
if weight >= 110 and age >= 16 and (days_since_donation == 0 or days_since_donation >= 56 ): # we use and if both condition is true
    print('Great, you are eligible to be a blood donor.')                                    # we use or if one condition is true


else:
    # print a message saying the user is not eligible
    print('Sorry, you are not eligible to be a blood donor.')

    # check if the user is under 16
    if age < 16:
        # Print if he is under 16 you can not donate or old enough
        print('You are not old enough')

    # check if the user's weight is under 110
    if weight < 110:
        # if the user is under 110 display you can not donate
        print('You  do not weight enough to be a blood donor')

    # check if the user donated blood less than 56 days ago
    if days_since_donation > 0 and days_since_donation < 56:
        # display a message saying that the user donated too recently
        print('You donated blood too recently. You must wait 56 days between donations.')

