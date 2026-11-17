import requests


# TO-DO
# ask user for ingredient
# make request to search for that ingredient
# print output neatly
# handle errors
#   errors in queries - no matching recipes
#   no query provided
#   API  server down

from pprint import pprint

print('Sandwich Recipe Search')
search_ingredients = input('Enter ingredients: ')

query_dictionary = {'query': search_ingredients}

url = 'https://recipe-1150.uc.r.appspot.com/search' # just the base URL


# response = requests.get(url, params=query_dictionary).json() # original one

server_response = requests.get(url, params=query_dictionary) # make request
# servers will send a status code with each response
# 404 not found
# 400 'bad request' - program, user has made an invalid request
# 500, 501 - server error
# 200 - ok!

print(server_response.status_code)

if server_response.status_code != 200: # if response is not ok
    print('Sorry, something went wrong.') # tell user
    exit() # quit program, nothing to do - don't continue to try process the response

response = server_response.json() # convert response to JSON

# pprint(response)

# handle the case of no recipe found
# response will be {'error': 'no recipe found'}

if 'error' in response: # does the response dictionary have an 'error' key?
    print(response)

else: # assume we have a recipe, get all the data and print it
    recipe_name = response['name']
    print('name: ' + recipe_name)

    description = response['description']
    print('description: ' + description)

    ingredients = response['ingredients']
    print() # empty line
    #print(ingredients)
    # print(type(ingredients))

    print(f'{'ingredient':<60} {'quantity'}') # table header
    print('-' * 75) # divider

    for ingredient, quantity in ingredients.items():
        #print(ingredient, quantity) # this is fine
        print(f'{ingredient:<65} {quantity}') # option - use a table

    instructions = response['instructions'] # a list, order is important
    # print(instructions)
    # print(type(instructions))
    print()
    print('instructions ')

    # print steps with numbers
    for index, step in enumerate(instructions):  # print steps with numbers
        print(f'{index+1}. {step}')