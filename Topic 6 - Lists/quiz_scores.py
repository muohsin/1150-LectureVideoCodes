
# Store the original scores for five quizzes in a list.
quiz_scores = [8, 4, 10, 9, 7]

# Ask the user which quiz they retook.
# int() converts the answer from text into a whole number.
quiz = int(input('Which quiz did you retake? '))

# Subtract 1 because Python list positions start at index 0.
index = quiz - 1

# Ask the user for their new score on the quiz.
score = int(input('What was your score on quiz 2? '))

# Replace the old score with the new score at the selected index.
quiz_scores[index] = score

# Display the updated list of quiz scores.
print(quiz_scores)
