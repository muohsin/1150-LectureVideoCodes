
# A list of integers (whole numbers).
lab_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# A list of temperatures recorded during the week.
temps = [78, 87.5, 67.7, 56.3, 66.3, 98.4, 67.9]

# Get the temperature recorded on the first day.
# Python starts counting list positions at 0.
first_day_temp = temps[0]

# Display the first day's temperature with a message.
print(f'The first day of the week was {first_day_temp}F')

# Change the temperature at index 3 to 66.3.
temps[3] = 66.3

# Display the updated list of temperatures.
print(temps)


# A list containing different types of data.
example = [False, 4, 1234.567, 'Hello']


# Create a list that contains other lists.
lists = [example, temps, lab_numbers, [1, 2, 3]]

# Display the complete list, including all the lists inside it.
print(lists)
