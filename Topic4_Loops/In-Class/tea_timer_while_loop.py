import time
import webbrowser


try:
    # Ask the user how many seconds they want the timer to run.
    # int() changes the answer from text into a whole number.
    seconds = int(input('Please enter the number of seconds: '))


    # Ask the user how they want to be notified when the timer is done.
    # We use while True so the program can keep asking if the answer is wrong.
    while True:
        # .lower() makes the answer lowercase.
        # This means "SILENT", "Silent", and "silent" will all work.
        mode = input('What kind of alert? Enter "silent" or "video": ').lower()


        # Check if the user entered one of the two choices we accept.
        if mode == 'silent' or mode == 'video':
            # break stops the loop because the user gave a valid answer.
            break

        # If the answer was not silent or video, ask the user again.
        else:
            print('Please enter "silent" or "video". Try again?')


    # Start counting the seconds one at a time.
    # The program waits one second before showing the next number.
    for seconds in range(seconds):
        print(str(seconds + 1) + 's')
        time.sleep(1)


    # Now check what alert the user selected.
    if mode == 'silent':
        # If they chose silent, just let them know the timer is finished.
        print('TIME IS UP!')


    # If they chose video, open the YouTube video in a web browser.
    else:
        webbrowser.open(
            'https://youtu.be/LjZxeSne67E?si=HjeOTsdeDJUigr7W'
        )


# If the user enters something that is not a whole number for the timer,
# this prevents the program from crashing and shows a helpful message.
except ValueError:
    print('Please enter a whole number.')