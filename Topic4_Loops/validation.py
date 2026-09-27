# while loop validation
# make sure the user's input is one of the valid choice

# survey student for how they get to campus
# walk, bus, drive, cycle

while True:
    # repeat this until the user enters valid info
    transport = input('How did you get to campus today? ').lower() # this converts lowercase before comparing to valid option

    # we are using transport before every word
    # because it will check if the input
    # we write is the one we need and if we put any other input
    # and remove transport it will not check if the input
    # is correct or wrong but will answer to you
    if transport == 'walk' or transport == 'cycle' or transport == 'bus' or transport == 'drive':
        # user has entered valid data
        break # stops the loop!
    else:
        print('Please enter either "walk" or "cycle" or "bus" or "drive"')

print('Thanks for answering the survey!')
print('You entered ' + transport)
# print(f'You entered {transport}')  # same with the first one