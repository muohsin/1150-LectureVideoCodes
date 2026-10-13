from flask import Flask, render_template

# __name__ is a built-in variable
# that stores the name of the program file

app = (Flask(__name__))

@app.route('/') # decorator
def hello_world():
    #return 'Hello, World!'
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)

