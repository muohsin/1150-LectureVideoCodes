# USING ELIF

quiz_score = float(input('please enter the quiz score, out of 100: '))

# convert quiz score to a letter grade

if quiz_score >= 90:
    print('Your letter grade is an A')
elif quiz_score >= 80:
    print('Your letter grade is a B')
elif quiz_score >= 70:
    print('Your letter grade is a C')
elif quiz_score >= 60:
    print('Your letter grade is a D')

else:
    print('Sorry, you failed the quiz')