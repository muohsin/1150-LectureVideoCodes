
# Each student took 3 quizzes

# Create a dictionary where each student's name is a key
# and their three quiz scores are stored in a list
quiz_scores = {
    'Al': [8, 9, 5],
    'Bettina': [6, 10, 10],
    'Cody': [7, 7, 9]
}

# Loop through the dictionary to get each student's name and scores
for student, list_of_scores in quiz_scores.items():

    # Display the student's name and their list of quiz scores
    print(f'Student {student} scores are {list_of_scores}')

# Get Cody's quiz scores from the dictionary
cody_scores = quiz_scores['Cody']

# cody_scores is a list, so we can use list operations on it

# Loop through Cody's scores and number each quiz starting at 1
for i, score in enumerate(cody_scores):

    # Display the quiz number and Cody's score
    print(f'On quiz {i + 1} Cody scored {score}')

# Find Cody's highest quiz score
cody_max = max(cody_scores)

# Display Cody's highest score
print(f'Cody\'s best score is {cody_max}')



# Get Bettina's quiz scores from the dictionary
bettina_scores = quiz_scores['Bettina']

# Find Bettina's lowest quiz score using min()
bettina_min = min(bettina_scores)

# Print Bettina's lowest quiz score
print(f"Bettina's lowest score is {bettina_min}")

