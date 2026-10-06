# example task - how many letters in a string

credit_card_number = '8686876868765668' # is 16 digits long

# can we count the letters without the len function?


counter = 0
for character in credit_card_number:
    # print(digits)
    counter = counter + 1

print('The length of the credit card number is ' + str(counter))

if counter != 16:
    print('The length is Invalid')
social_security_number = '123-23-2222' # should be 11 characters

counter = 0
for character in social_security_number:
    # print(digits)
    counter = counter + 1

print('The length of the social security number is ' + str(counter))