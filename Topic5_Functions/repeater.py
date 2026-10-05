# Define the main function
def main():
    # Ask the user to enter a string
    string = input('Please enter a string: ')

    # Ask the user how many times to repeat the string
    repeat = int(input('How many times to repeat? '))

    # Call the string_repeater function with two arguments
    result = string_repeater(string, repeat)

    # Print the repeated string
    print(result)


# Define a function with two parameters
def string_repeater(text, n):
    # Repeat the text n times
    repeated_string = text * n

    # Return the repeated string
    return repeated_string


# Call the main function to run the program
main()