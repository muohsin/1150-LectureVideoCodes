
# Store the number of credits for each class in a list.
credits_per_class = [4, 3, 3, 2]

# Start the total at zero before adding the credits.
total = 0

# Go through each class and add its credits to the total.
for credit_count in credits_per_class:
    total = total + credit_count

# Display the total number of credits.
print(total)

# # Use Python's sum() function to calculate the same total.
# total_with_sum_function = sum(credits_per_class)
#
# # Display the total calculated by sum().
# print(total_with_sum_function)

# Check whether the student is taking 12 or more credits.
if total >= 12:
    print('You are full time')

# If the student has fewer than 12 credits, check for 6 or more.
elif total >= 6:
    print('You are part time')

# If neither condition is true, the student has fewer than 6 credits.
else:
    print('You are less than part time.')
