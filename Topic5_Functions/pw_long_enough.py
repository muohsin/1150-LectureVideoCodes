# Define a function called is_password_long_enough
# password is the PARAMETER
def is_password_long_enough(password):

    # Check if the password has at least 8 characters
    if len(password) >= 8:
        # Return True if the password is long enough
        return True
    else:
        # Return False if the password is not long enough
        return False


# Define the main function
def main():

    # Store the password
    password = 'kittens'

    # Call the function
    # password is the ARGUMENT being passed to the function
    if is_password_long_enough(password):

        # Print if the password is long enough
        print(f'The password "{password}" is long enough.')
    else:

        # Print if the password is NOT long enough
        print(f'The password "{password}" is NOT long enough.')


# Call the main function
main()