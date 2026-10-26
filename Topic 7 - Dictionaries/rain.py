
# CONCEPT 1: LIST
# Store the months we want to collect rainfall data for
months = ['June', 'July', 'August']

# CONCEPT 2: DICTIONARY
# Create an empty dictionary to store each month's rainfall
rainfall_per_month = {}

# CONCEPT 3: FOR LOOP
# Repeat the following instructions for every month in the list
for month in months:

    # CONCEPT 4: USER INPUT AND TYPE CONVERSION
    # Ask the user for rainfall and convert the answer to a float
    rain = float(input(f'How much rain fell in {month}? '))

    # CONCEPT 5: ADDING KEY-VALUE PAIRS
    # Store the rainfall amount using the month as the key
    rainfall_per_month[month] = rain

# CONCEPT 6: PRINTING
# Display the complete dictionary
print(rainfall_per_month)

# CONCEPT 7: DICTIONARY ITEMS AND LOOPING
# Get each month and its rainfall amount
for month, rain in rainfall_per_month.items():

    # Use an f-string to display the information
    print(f'In {month} it rained {rain} inches')

# CONCEPT 8: SUM AND DICTIONARY VALUES
# Add all rainfall amounts to calculate the total
total = sum(rainfall_per_month.values())

# Display the total rainfall
print(f'The total rain is {total:.2f} inches')

# CONCEPT 9: LENGTH OF A DICTIONARY
# Count how many months have rainfall data
number_of_months = len(rainfall_per_month)

# CONCEPT 10: ARITHMETIC
# Calculate average rainfall by dividing total by number of months
average = total / number_of_months

# CONCEPT 11: F-STRINGS AND NUMBER FORMATTING
# Display the average to two decimal places
print(f'The average for {number_of_months} months is {average:.2f} inches')
