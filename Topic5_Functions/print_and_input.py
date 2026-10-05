# Create a function that takes a name and creates a greeting message
# define the greeting function
def greeting(name):
    # Create a greeting using the name
    message = f'Hello {name}'

    # Return the greeting message
    return message

# define the main function
# Create the main function
def main():
    # Store the username
    username = 'Zoe'


    # greeting(message) calls the greeting function
    # Call the greeting function and store the returned message
    hello_message = greeting(username)

    # Print the greeting message
    print(hello_message)


# Call the main function to run the program
main()