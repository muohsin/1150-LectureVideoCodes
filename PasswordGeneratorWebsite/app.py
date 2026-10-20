from flask import Flask, render_template, request
import string
import random

# __name__ is a built-in variable
# that stores the name of the program file

app = (Flask(__name__))

@app.route('/') # decorator
def hello_world():
    #return 'Hello, World!'
    return render_template("home.html")

@app.route('/generate_password')
def generate_user_password():
    # get the length entered
    length = int(request.args.get('password_length'))
    print(length)

    # generate a password of that length
    characters = generate_password_characters()
    password = generate_password(length, characters)
    print(password)


    # show the user the password by
    # rendering the password template
    return render_template('password.html', password=password)


def generate_password_characters():
    # TASK - set up the characters to choose from for the password
    letters = string.ascii_letters # 'abcdefghijklmnopqrstuvwxyzABCDEF1234567890GHIJKLMNOPQRSTUVWXYZ'
    numbers = string.digits # optional
    # symbols = string.punctuation  # optional - have to be careful to only use allowed symbols
    symbols = '#&_!?'  # so you could make a string of allowed special characters
    # Optional extra question - why don't passwords allow some special characters? More info: "SQL injection"
    # Optional extra question - why are longer, more complex passwords harder to guess?
    all_characters = letters + numbers + symbols   # just for debugging
    return all_characters


def generate_password(password_length, letters):
    # TASK Random character generation to make password
    password = ''  # start with empty string

    for letter in range(password_length):  # repeat once for each letter needed
        random_letter = random.choice(letters)
        print(random_letter)
        password = password + random_letter

    return password  # outputs the password - to be stored in the main function


def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)

