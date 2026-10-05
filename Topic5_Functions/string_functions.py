# Define the main function
def main():
    # Ask the user to enter the number of miles
    miles = float(input('Please enter a number of miles'))

    # Call the miles_to_kilometers function and store the result
    kilometers = miles_to_kilometers(miles)

    # Display the miles and converted kilometers
    print(f'{miles} miles is equal to {kilometers} kilometers.')


# Define a function that converts miles to kilometers
def miles_to_kilometers(miles):
    # Convert miles to kilometers
    km = miles * 1.60934

    # Return the converted value
    return km


# Call the main function to run the program
main()