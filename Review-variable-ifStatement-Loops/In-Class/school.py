
        ## we are using this one ##
# Write a program to ask the user these questions.

# Ask for the wind chill forecast for 6 a.m.
# You can ask for a number, or a yes/no questions.
# What do you think will work best?

# Ask for the amount of snow in the last 12 hours.
# You can ask for the number of inches, or you can ask a yes/no question.
# What do you think will work best?

# Use an if-statement to decide if school should cancel classes or not.
# Your program should print "School is in" or "School is cancelled".

wind_chill = int(input('what will be the wind chill forecast at 6 AM ? ')) # create variable(wind chill) and ask the user to store data.

amount_of_snow = float(input('how many inches of snow will fall in the last 12 hours? ')) # create variable(amount of snow) and ask the user to store data.

if wind_chill <= -35: # check if wind chill is less than or equal -35.
    print('school is cancelled') # display the message.

elif amount_of_snow >= 4: # check if amount of snow is greater than four.
    print('school is cancelled') # display the message.

else: # otherwise, if the previous statements were False.
    print('school is in') # display this message.


# we will think it after class to figure it out :
