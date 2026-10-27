# Storing data as a list - have the names of the ingredients
# but how much of each?
# Lists use [ ] to define them
# ingredients = ['Bread slices', 'Cheese slices', 'Tablespoons of butter']

# Dictionaries in Python - like a list, but you can store one more
# piece of information for each item in that list

# dictionaries use { }
# A list of key-value pairs. Use : to connect key and value
# use , to separate key-value pairs
# the keys need to be unique. so, use the ingredient names as keys
# even though we might describe information about an ingredient and quantity as
# '2 slices of bred'

ingredients = {
    'Bread slices': 2,  # First thing is a "key", associated with a "value"
    'Cheese slices': 2,
    'Tablespoons of butter': 1.5,
    #'Bread slices': 4  # not allowed to have duplicates keys. This will overwrite the first one
}

print(ingredients)

# how many servings

servings = int(input("How many servings to make? "))

# use the dictionary, calculate total amount of each ingredient
# and display the total for each ingredient.

for ingredient in ingredients: # by default, prints loop over just the keys
    print(ingredient) # print just the keys (ingredient names) - not the values (quantities)

# how do we get the values - the quantities? there's two ways (other way in videos)
# next: I want to save the quantities for multiple servings
# start in a new dictionary
adjusted_ingredients = {} # make a new , empty dictionary
# loop will add the ingredients and total quantity

for ingredient, quantity in ingredients.items():
    #print(ingredient, quantity)
    # example: quantity = 2 slices of bread, servings = 3 people: 2 * 3 = 6
    total_quantity = quantity * servings
    # print( ingredient, total_quantity) # basic print statement
    print(f'{ingredient}: {total_quantity}') # format string
    # assign the value to the value of a key in the dictionary
    adjusted_ingredients[ingredient] = total_quantity

    print(adjusted_ingredients)

