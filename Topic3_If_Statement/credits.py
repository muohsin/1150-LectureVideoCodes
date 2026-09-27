number_of_credits = int(input('How many credits are you taking this semster? '))

while number_of_credits < 0:
    print('Error - Please enter 0 or a positive number ')
    # if we don't have this it will continue repeating again and again
    number_of_credits = int(input('How many credits do you want this semster? '))

if number_of_credits >= 12:
    print('You are a full time student.')
elif number_of_credits >= 6:
    print('You are a half-time student.')
else:
    print('You are less than half-time student.')
