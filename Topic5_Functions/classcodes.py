# This function checks the class code and tells us which year it belongs to
def class_year(class_code):

    # If the class code is from 1000 to 1999, it is a first-year class
    if 1000 <= class_code <= 1999:
        return 'First Year'

    # If the class code is from 2000 to 2999, it is a second-year class
    elif 2000 <= class_code <= 2999:
        return 'Second Year'

    # If the class code does not fit either range, it is not valid
    else:
        return 'Invalid Code'


# This is the main part of the program
def main():

    # Ask the user to enter the class code they are taking
    class_code = int(input('Please enter your class code: '))

    # Send the class code to the function and save the answer
    result = class_year(class_code)

    # Show the answer returned by the function
    print(result)


# Start the program by calling the main function
main()