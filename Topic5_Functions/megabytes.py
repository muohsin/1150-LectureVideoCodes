""" A program that uses megabytes to convert bytes into megabytes """


# Define a function that converts megabytes to bytes
def megabytes_to_bytes(megabytes):
    # Multiply megabytes by 1,000,000 to get bytes
    bytes = megabytes * 1000000

    # Return the number of bytes
    return bytes


# Define the main function
def main():
    # Call the conversion function with 10 megabytes
    b = megabytes_to_bytes(10)

    # Print the result
    print(b)


# Call the main function to run the program
main()