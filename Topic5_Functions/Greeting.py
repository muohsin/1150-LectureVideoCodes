def greeting(name):
    # Create a message using the name given to the function.
    message = f'Hello {name}'

    # Send the message back to the place where the function was called.
    return message


def main():
    # Store the user's name in a variable.
    username = 'Zoe'

    # Call the greeting function and give it the username.
    # The returned message is saved in hello_message.
    hello_message = greeting(username)

    # Display the message on the screen.
    print(hello_message)


# Call main to start the program.
main()