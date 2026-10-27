
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/calculate')
def calculate():
    # How many servings did the user ask for?
    form_data_dictionary = request.args.to_dict()
    print(form_data_dictionary)

    servings_string = form_data_dictionary['servings']
    servings = int(servings_string)

    ingredients = {
        'Bread slices': 2,
        'Cheese slices': 2,
        'Tablespoons of butter': 1.5
    }

    # Create a new, empty dictionary
    adjusted_ingredients = {}

    # Calculate the quantities needed for each ingredient
    for ingredient, quantity in ingredients.items():
        total_quantity = quantity * servings
        adjusted_ingredients[ingredient] = total_quantity

    return render_template(
        'results.html',
        adjusted_ingredients=adjusted_ingredients
    )


# Restart the app automatically when code changes
app.run(debug=True)
