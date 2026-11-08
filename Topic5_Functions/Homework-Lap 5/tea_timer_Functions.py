
# Question 2: Tea Timer Using Functions

import time
import webbrowser


# This function asks the user how many seconds they want the timer to run.
# It keeps asking until the user enters a valid whole number greater than 0.
def get_time():
    while True:
        try:
            seconds = int(input('Enter the number of seconds: '))

            # Make sure the user enters a positive number.
            if seconds > 0:
                return seconds
            else:
                print('Please enter a number greater than 0.')

        # This handles the error if the user enters letters or other invalid input.
        except ValueError:
            print('Please enter a whole number.')


# This function asks the user how they want to be notified.
# The user can choose silent mode or video mode.
def get_mode():
    while True:
        mode = input('What kind of alert? Enter silent or video: ').lower()

        # Check if the user entered one of the two choices.
        if mode == 'silent' or mode == 'video':
            return mode
        else:
            print('Please enter "silent" or "video". Try again!')


# This is the main function that runs the tea timer program.
def main():

    # Get the number of seconds and the alert mode from the functions above.
    seconds = get_time()
    mode = get_mode()

    # Start counting down one second at a time.
    # The program waits one second before displaying the next number.
    for second in range(seconds):
        print(str(second + 1) + 's')
        time.sleep(1)

    # Check which alert the user selected after the timer finishes.
    if mode == 'silent':

        # If the user chose silent mode, display a message.
        print('TIME IS UP!')

    else:

        # If the user chose video mode, open a YouTube video.
        webbrowser.open('https://youtu.be/LjZxeSne67E?si=HjeOTsdeDJUigr7W')


# Call the main function to start the program.
main()
