credits_taken = int(input('How many credits are you taking? '))
print(credits_taken)

credits_taken_last_semester = int(input('How many credits were taken last semester? '))

print(credits_taken_last_semester + credits_taken)

total_credits = credits_taken + credits_taken_last_semester

print('The total credits will be ' + str(total_credits) + ' in this and last semesters ')
