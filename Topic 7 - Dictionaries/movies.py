
# Create a dictionary that stores movie names and their ratings
movies_ratings = {
    'Up': 8,          # The movie 'Up' has a rating of 8
    'Spider-man': 7,   # The movie 'Spider-Man' has a rating of 7
    'Groundhog': 8,     # The movie 'Groundhog' has a rating of 8
    'Batman': 9
    }

# Display the entire dictionary in the output
print(movies_ratings)


# Print a movie rating.
# Get the rating for Spider-Man from the movies_ratings dictionary
# and store that rating in a variable called spiderman_rating.
spiderman_rating = movies_ratings['Spider-man']

# Print the rating stored in the spiderman_rating variable.
print(spiderman_rating)


# Try to get a rating for a movie that does not exist in the dictionary
# Batman is not currently a key in movies_ratings # error without get
batman_rating = movies_ratings.get('Batman') # prints none

# Print Batman's rating
print(batman_rating)


# Check whether Batman has a rating in the dictionary
if batman_rating is None:

    # Display this message if Batman has no rating
    print('There is no rating for Batman in the dictionary.')

else:
    # Display this message if Batman has a rating
    print('There is a rating for Batman, and it is ' + str(batman_rating))

# check whether Up movies has a rating in the dictionary
up_rating = movies_ratings.get('Up')
#display
print(up_rating)


# Check whether 'Up' exists as a key in the movies_ratings dictionary
if 'Up' in movies_ratings:

    # Print this message if 'Up' exists in the dictionary
    print('Up is one of the movies')

else:
    # Print this message if 'Up' does not exist in the dictionary
    print('Up is Not one of the movies')



# Check whether 'Inside Out' exists in the movies_ratings dictionary
if 'Inside Out' in movies_ratings:

    # Print this message if Inside Out is found
    print('Inside Out is one of the movies')

else:
    # Print this message if Inside Out is not found
    print('Inside Out is NOT one of the movies.')



# Update the rating for the movie with the key 'Spider-Man'
# Change Spider-Man's rating from 7 to 9
movies_ratings['Spider-man'] = 9

# Print the entire dictionary to see the updated rating
print(movies_ratings)



# Add a new key to the movies_ratings dictionary
# Add the movie 'Bill and Ted' with a rating of 8
# If the key does not exist, Python creates a new key-value pair.
movies_ratings['Bill and Ted'] = 8  # Compare this with line 13

# Print the dictionary to see the new movie and its rating
print(movies_ratings)



# Loop through each movie name
for movie_name in movies_ratings:

    # Print the movie name
    print(movie_name)



# Loop over the movie names (keys) and ratings (values)
for movie_name, rating in movies_ratings.items():

    # Print each movie's name and rating using an f-string
    print(f'{movie_name} has a rating of {rating} out of 10')


print(movies_ratings)
batman_rating = movies_ratings.pop('Batman')
print(movies_ratings)
print(batman_rating)

if 'The Avengers' in movies_ratings:
    movies_ratings.pop('The Avengers')

print(movies_ratings)





