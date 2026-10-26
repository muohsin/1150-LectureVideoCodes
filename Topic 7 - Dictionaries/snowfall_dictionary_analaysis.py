
# Create a list containing the months we want to track
# [] is used to create a list
winter_months = [
    'October', 'November', 'December', 'January',
    'February', 'March', 'April'
]

# Create an empty dictionary to store snowfall amounts
# {} creates an empty dictionary
snowfall = {}

# Loop through each month in the winter_months list
for month in winter_months:

    # Ask the user how much snow fell during the month
    # input() gets information from the user
    # float() converts the input into a decimal number
    snow = float(input(f'How much snow in {month}, in inches? '))

    # Store the snowfall amount using the month as the key
    snowfall[month] = snow

# Print a blank line for better readability
print()

# Display a heading before showing the collected information
print('Here is all of the data you entered:')

# Loop through the dictionary's keys and values
# .items() gives us both the month and its snowfall amount
for month, snow in snowfall.items():

    # Display the month and its snowfall amount
    print(f'In {month} there was {snow} inches of snow.')

# Get all snowfall amounts using .values()
# sum() adds all the snowfall amounts together
total_snow = sum(snowfall.values())

# len() counts the number of entries in the dictionary
months = len(snowfall)

# Calculate the average snowfall per month
average = total_snow / months

# Print a blank line before the final results
print()

# Display the total snowfall for all recorded months
print(f'The total amount of snow in {months} months is {total_snow} inches.')

# Display the average snowfall rounded to two decimal places
# :.2f formats the number to show two digits after the decimal point
print(f'The average amount of snow per month is {average:.2f} inches')
