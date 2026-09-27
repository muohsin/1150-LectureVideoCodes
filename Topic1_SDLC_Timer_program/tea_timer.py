# Add the time module to allow python to count
# a number of seconds

import time


try:
    # Create a variable called "seconds"
    # Ask the user for the number of seconds
    # Convert the user's input to a number
    # int means integer nimber, which are whole numbers
    seconds = int(input('Enter the number of seconds: '))

    # Program "sleeps" for the number of seconds the user
    # enter. The program uses the data stored in thr "seconds"
    # variables to know how long to sleep for.
    # this provides the timer functionality.
    time.sleep(seconds)

    # displays a message to the user.
    print('TIME IS UP!')

except ValueError:
    print('Please enter a number!')

