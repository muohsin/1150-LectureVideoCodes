# USING IF ELSE


parking_time = float(input('How many hour have you parked? '))

# The max parking time allowed is 2 hours.

if parking_time >= 2:
    print('Warning! You should move your car.')
    # add how many hours you went over
    time_over = parking_time - 2
    print('you have exceeded ' + str(time_over) + ' over.')
else:
    print('You are okay for parking, you still have time.')

    #add how many hours you've left
    time_left = 2 - parking_time
    print('You have ' + str(parking_time) + ' hours left.')

print('This is the end of the program.')