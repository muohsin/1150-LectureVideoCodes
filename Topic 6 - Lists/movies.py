# Import random so we can shuffle the movie list.
import random

# Create a list containing four movie titles.
movies = ['Fargo', 'Up', 'Rocky', 'Jaws']

# Arrange the movie titles in alphabetical order.
movies.sort()

# Reverse the sorted list so the titles appear in reverse order.
movies.reverse()

# Go through the list one movie at a time.
for movie in movies:

    # Display the current movie title.
    print(movie)



# Add a new movie called Spiderman to the end of the list.
movies.append('Spiderman')

# Display the list to see the new movie.
print(movies)

# Add another movie called Lion King to the end of the list.
movies.append('Lion King')

# Display the list again to see both new movies.
print(movies)

# Count how many movies are currently in the list.
number_of_movies = len(movies)

# Display the total number of movies using an f-string.
print(f'There are {number_of_movies} movies in the list.')

# Remove Rocky from the list.
movies.remove('Jaws')

# Display the updated list after removing the movie.
print(movies)



# This would cause an error because Frozen is not in the list.
# movies.remove('Frozen')

# Remove the first movie from the list using index 0.
last_movie = movies.pop()

# Display the list after removing the first movie.
print(movies)
print(last_movie)


# Shuffle the movies into a random order.
random.shuffle(movies)

# Print the movies as a numbered list.
for index, movie in enumerate(movies):
    print(f'{index + 1}: {movie}')

