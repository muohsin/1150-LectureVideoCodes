
# Create a list with five quiz scores, all starting at 0.
quiz_scores = [0] * 5

# Display the starting scores.
print(quiz_scores)

# # Repeat the loop five times, once for each quiz.
# for quiz in range(5):
#     # Ask the user to enter a score and convert it to an integer.
#     score = int(input(f'Enter score for quiz {quiz+1}: '))
#
#     # Store the score in the correct position in the list.
#     quiz_scores[quiz] = score

# Get each quiz's index and its current score.
for quiz, score in enumerate(quiz_scores):
    # Ask the user to enter a new score for this quiz.
    new_score = int(input(f'Enter score for quiz {quiz+1}: '))

    # Replace the old score with the new score.
    quiz_scores[quiz] = new_score

# Display a message before showing the final scores.
print('You score are:')

# Display the updated quiz scores.
print(quiz_scores)
