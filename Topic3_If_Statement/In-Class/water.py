"""
Example program with variables and input -

Hydration: keeping track of water you drink

Let's say you want to drink 10 cups of water a day.
Let's ask the user how many cup of water they drank today,
and calculate how many more they are advised to drink today.

<-- this is another way to add a comment to Python code, three double quotes

Example program with variables and input -

Hydration: keeping track of water you drink

Let's say you want to drink 10 cups of water a day.
Let's ask the user how many cups of water they drank today,
and calculate how many more they are advised to drink today.

For example, they may enter 3 cups of water.
Store the number 3, do math to subtract 10-3, we'll get 7
Display the result to the user.

End your comment with three double quotes

Why build such a simple program that we could solve without Python?
1. So we can easily test it works
2. So we can focus on the code, and not the complexities of the problem
3. Real-world programs are often built by starting with a very simple program, and adding
   features, details, complexity.

"""



# Ask the user how many cups of water they have drunk
# we have a variable (program_name), a string (str) variable storing text data
program_name = 'Hydration Program'

print(program_name)

# we have a variable (cups)
cups = float(input('How many cups of water have you drunk up so far today? '))


target_number_of_cups = 10

print(cups)

# todo- how many to handle numbers larger than 10
# what about really big numbers?
# what other types of numbers are invalid

# math - how many more cups to drink?
# cups_to_drink = 10 - cups # old version
cups_to_drink = target_number_of_cups - cups # new version using a variable

# decision if we need to do math and figure out how many more cups
# decision is based on if the number of cups is less than 10

# do validation first before processing data

if cups > 50:  # you can choose a different number here. what is the most a user could reasonably drin?
    print('Please enter a valid number, ' + str(cups) + ' is too many.')

# to not give us a negative numbers
elif cups < 0:
    print('Please enter a valid number!')

elif cups < 10:
    # intendations/tabs helps to work the code for that sections
    cups_to_drink = target_number_of_cups - cups

    # output results to user how many more cups?
    print('You still need to drink ' + str(cups_to_drink) + ' cups of water today')

# tell user they have met their goal
else:
    print('You met your goal today!')



