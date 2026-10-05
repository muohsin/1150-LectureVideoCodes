# Define the main function
def main():
    # Loop through the numbers from 0 to 9
    for number in range(10):
        # Call the cube function and store the result
        c = cube(number)

        # Print the cube
        print(c)


# Define a function that finds the cube of a value
def cube(value):
    # Multiply the value by itself three times
    cube_value = value * value * value

    # Return the cube value
    return cube_value


# Call the main function to run the program
main()