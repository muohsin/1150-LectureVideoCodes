# If statements 1 - Favorite

# Write a program that asks for your favorite video game. Python's favorite video game is Tetris.

# Use an if statement to check if your favorite game is the same as Tetris.
# If it is, print the message "Your favorite video game is the same as mine!"
# Else, print the message "We like different video games."


favorite_video_game = input('What is your favorite video game? ')
# single = is an assignment
favorite_video_game = favorite_video_game.title() # upper case_sensitive

# make a decision based on the value of a variable
# double == is testing for equalities
if favorite_video_game == 'Tetris':
    print('Your favorite video game is the same as mine!')

else:
    print('We like different video games. My favorite is Tetris.')