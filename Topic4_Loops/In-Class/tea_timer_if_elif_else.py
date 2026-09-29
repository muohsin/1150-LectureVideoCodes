# import a web browser to play music when the time is up
# use one of YouTube/music sound to play with it
import webbrowser


# Add the time module to allow python to count
# a number of seconds
import time


try:
    # Create a variable called "seconds"
    # Ask the user for the number of seconds
    # Convert the user's input to a number
    # int means integer number, which is a whole number
    seconds = int(input('Enter the number of seconds: '))


    # ask the user what they want to happen when the timer is finished
    user_choice = input('Enter silent mode or video mode: ')


    # Program "sleeps" for the number of seconds the user
    # enters. The program uses the data stored in the "seconds"
    # variable to know how long to sleep for.
    # This provides the timer functionality.
    time.sleep(seconds)


    # check if the user chose silent mode
    if user_choice == 'silent mode':
        # display a message when timer is finished
        print('Time is up!')


    # check if the user chose video mode
    elif user_choice == 'video mode':
        # the url variable will open a new web browser and will
        # play music when the tea timer is up.
        url = 'https://youtu.be/pxpyElm1mHU?si=vKEHkU6NH69EL6WJ'
        webbrowser.open(url)


    # if the user did not enter either of the two choices
    else:
        # tell the user to enter one of the valid choices
        print('Please enter either silent mode or video mode.')


# handle the error if the user does not enter a valid integer
except ValueError:
    # tell the user that they need to enter a number
    print('Please enter a number!')



