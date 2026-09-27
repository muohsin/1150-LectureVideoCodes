# Ask the user to enter their weight and convert the input from text to a decimal number.
weight = float(input('Please enter your weight in pounds: '))

# Ask the user to enter their age and convert the input from text to a whole number.
age = int(input('Please enter your age in years: '))

# Create a variable to track whether the user meets the 56-day donation requirement.
# Start with False because the user has not been checked yet.
donation_frequency_eligibility = False

# Ask the user whether they have ever donated blood before.
donated_before = input('Have you donated blood before? Enter "yes" or "no": ')

# Check whether the user has donated blood before.
if donated_before == 'yes':

    # Ask how many days have passed since the user's last blood donation
    # and convert the answer from text to a whole number.
    days_since_last_donation = int(input('Enter number of days since last donation: '))

    # Check whether the user has waited at least 56 days since their last donation.
    if days_since_last_donation >= 56:

        # Set the eligibility variable to True because the user waited long enough.
        donation_frequency_eligibility = True

    else:

        # Keep the eligibility variable False because the user donated too recently.
        donation_frequency_eligibility = False

else:

    # Set the eligibility variable to True because a person who has never donated
    # does not need to wait 56 days before their first donation.
    donation_frequency_eligibility = True

# Check that the user weighs at least 110 pounds, is at least 16 years old,
# and meets the 56-day donation requirement.
if weight >= 110 and age >= 16 and donation_frequency_eligibility == True:

    # Display a message telling the user that they meet all requirements.
    print('You are eligible to be a blood donor')

else:

    # Display a message telling the user that they do not meet all requirements.
    print('You are not eligible to be a blood donor')

    # Check whether the user's age is below the minimum age of 16.
    if age < 16:

        # Explain that the user is too young to donate blood.
        print('You are not old enough')

    # Check whether the user's weight is below the minimum weight of 110 pounds.
    if weight < 110:

        # Explain that the user does not meet the minimum weight requirement.
        print('You do not weigh enough to be a blood donor')

    # Check whether the user has donated before and has waited less than 56 days.
    if donated_before == 'yes' and days_since_last_donation < 56:

        # Explain that the user's previous donation was too recent.
        print('You donated blood too recently. You must wait 56 days between donations.')