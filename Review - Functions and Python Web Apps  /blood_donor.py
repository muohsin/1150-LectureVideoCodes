# To donate blood, you must be 17 or older and weigh at least 110 pounds.

# Interact with the user by asking for their information.


def main():
    # Ask the user to enter their age in years.
    # int() converts the answer from text into a whole number.
    age = int(input('Please enter your age, in years: '))

    # Ask the user to enter their weight in pounds.
    # We use int() because the program expects a whole number.
    weight = int(input('Please enter your weight, to the nearest pound: '))

    # Call the check_donor_eligibility function and give it
    # the user's age and weight so it can check the requirements.
    # The function returns True or False, which we store in eligible.
    eligible = check_donor_eligibility(age, weight)

    # Check the result returned by the function.
    # If eligible is True, display the positive message.
    if eligible:
        print('Great! You are eligible!')

    # If eligible is False, display the message below instead.
    else:
        print('Sorry, you are not eligible.')


# This function receives the age and weight from main().
# It uses them to decide whether the person meets the requirements.
def check_donor_eligibility(age, weight):

    # Check whether the person is at least 17 years old
    # AND weighs at least 110 pounds.
    # Both conditions must be True to qualify.
    if age >= 17 and weight >= 110:

        # Return True to tell main() that the person qualifies.
        return True

    else:
        # Return False if either requirement is not met.
        return False


# Call main() to start the program.
main()
