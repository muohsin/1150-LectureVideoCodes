# Define the main function
def main():
    # Store the number of credits completed
    credits_completed = 34

    # Store the name of the college
    college = 'Minneapolis College'

    # Call the report function with credits and college
    report(credits_completed, college)

    # The order of the arguments matters
    # report(college, credits_completed)


# Define a function with two parameters
def report(cr, col):
    # Print the name of the school
    print(f'Your school is {col}')

    # Calculate and print the credits needed to graduate
    print(f'You need {60 - cr} credits to graduate')


# Call the main function to run the program
main()