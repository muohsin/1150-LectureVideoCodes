# Example task - how many letters in a string?


def string_length(unknown_length_string):
    # Start the counter at 0 because we have not counted anything yet.
    counter = 0

    # Go through the string one character at a time.
    for character in unknown_length_string:
        # print(character)  # This would print each character as we go.

        # Add 1 to the counter for every character in the string.
        counter = counter + 1

    # Return the total number of characters after the loop is finished.
    return counter

def main():
    credit_card_number = '4342543543454345'  # Is it 16 digits long?

    # Can we count the letters without the len function?
    # Yes - using a counter variable and a loop.

    # Call the function and save the returned value in a new variable.
    length = string_length(credit_card_number)

    # TODO check length
    # Print the number of characters in the credit card number.
    print('The length of the credit card is ' + str(length))

    # Check if the credit card number is NOT 16 characters long.
    if length != 16:
        print('The length is invalid')

    social_security_number = '123-12-1234'  # Should be 11 characters

    # TODO check length
    # Use the same function to count the characters in the Social Security number.
    length = string_length(social_security_number)

    # Print the number of characters in the Social Security number.
    print('The length of the social security number is ' + str(length))

    # Check if the Social Security number is NOT 11 characters long.
    if length != 11:
        print('The length is invalid')

main() # call the main function to start the program